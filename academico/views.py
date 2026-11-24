from django.shortcuts import render, redirect, get_object_or_404
from django.forms import modelform_factory
from django.http import Http404
from django.db.models.deletion import ProtectedError
from django.contrib import messages
from .models import Estudiante, Docente, Asignatura, Matricula, Calificacion
MODULOS = {'estudiantes': Estudiante, 'docentes': Docente, 'asignaturas': Asignatura, 'matriculas': Matricula, 'calificaciones': Calificacion}
def modelo(modulo):
    if modulo not in MODULOS:
        raise Http404()
    return MODULOS[modulo]
def inicio(request):
    return render(request,'inicio.html',{'totales':[(k,v.objects.count()) for k,v in MODULOS.items()]})
def listado(request, modulo):
    m = modelo(modulo)
    campos = [f for f in m._meta.fields if f.name != 'id']
    filas = [(obj.pk,[getattr(obj,f.name) for f in campos]) for obj in m.objects.order_by('pk')]
    return render(request,'listado.html',{'modulo':modulo,'campos':campos,'filas':filas})
def editar(request, modulo, pk=None):
    m = modelo(modulo)
    obj = get_object_or_404(m,pk=pk) if pk is not None else None
    Form = modelform_factory(m, fields='__all__')
    form = Form(request.POST if request.method=='POST' else None, instance=obj)
    for campo in form.fields.values():
        campo.widget.attrs['class'] = 'form-control'
    if request.method=='POST' and form.is_valid():
        form.save()
        messages.success(request,'Registro guardado.')
        return redirect('listado',modulo=modulo)
    return render(request,'formulario.html',{'form':form,'modulo':modulo,'editando':obj is not None})
def eliminar(request, modulo, pk):
    obj = get_object_or_404(modelo(modulo),pk=pk)
    if request.method=='POST':
        try:
            obj.delete()
            messages.success(request,'Registro eliminado.')
        except ProtectedError:
            messages.error(request,'No se puede eliminar: existen registros relacionados.')
        return redirect('listado',modulo=modulo)
    return render(request,'eliminar.html',{'obj':obj,'modulo':modulo})
