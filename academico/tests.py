from django.test import TestCase
from django.forms import modelform_factory
from .models import Estudiante, Docente, Asignatura, Matricula, Calificacion
class AcademicoTests(TestCase):
    def setUp(self):
        self.e=Estudiante.objects.create(cedula='1234567890',nombres='Ana',apellidos='Prueba',correo='ana@example.com')
        d=Docente.objects.create(cedula='1234567891',nombres='Luis',apellidos='Prueba',correo='luis@example.com',especialidad='Software')
        a=Asignatura.objects.create(codigo='POO',nombre='Programación',docente=d)
        self.m=Matricula.objects.create(estudiante=self.e,asignatura=a,periodo='2026-2')
    def test_paginas(self):
        for ruta in ('/','/estudiantes/','/docentes/','/asignaturas/','/matriculas/','/calificaciones/'):
            self.assertEqual(self.client.get(ruta).status_code,200)
    def test_nota_invalida(self):
        F=modelform_factory(Calificacion,fields='__all__')
        self.assertFalse(F({'matricula':self.m.pk,'nota':101}).is_valid())
    def test_matricula_duplicada(self):
        F=modelform_factory(Matricula,fields='__all__')
        self.assertFalse(F({'estudiante':self.e.pk,'asignatura':self.m.asignatura_id,'periodo':self.m.periodo}).is_valid())
    def test_registrar_nota(self):
        r=self.client.post('/calificaciones/nuevo/',{'matricula':self.m.pk,'nota':85})
        self.assertEqual(r.status_code,302)
        self.assertEqual(Calificacion.objects.get().nota,85)
    def test_eliminar_protegido(self):
        self.client.post(f'/estudiantes/{self.e.pk}/eliminar/')
        self.assertTrue(Estudiante.objects.filter(pk=self.e.pk).exists())
