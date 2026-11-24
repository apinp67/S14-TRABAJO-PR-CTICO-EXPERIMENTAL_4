from django.contrib import admin
from .models import Estudiante, Docente, Asignatura, Matricula, Calificacion
admin.site.register([Estudiante, Docente, Asignatura, Matricula, Calificacion])
