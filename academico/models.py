from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator, RegexValidator

class Persona(models.Model):
    cedula = models.CharField('Cédula', max_length=10, unique=True, validators=[RegexValidator(r'^\d{10}$', 'Ingrese 10 dígitos.')])
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    correo = models.EmailField(unique=True)
    class Meta:
        abstract = True
    def __str__(self):
        return f'{self.apellidos} {self.nombres}'

class Estudiante(Persona):
    pass

class Docente(Persona):
    especialidad = models.CharField(max_length=100)

class Asignatura(models.Model):
    codigo = models.CharField('Código', max_length=20, unique=True)
    nombre = models.CharField(max_length=100)
    docente = models.ForeignKey(Docente, on_delete=models.PROTECT)
    def __str__(self):
        return self.nombre

class Matricula(models.Model):
    estudiante = models.ForeignKey(Estudiante, on_delete=models.PROTECT)
    asignatura = models.ForeignKey(Asignatura, on_delete=models.PROTECT)
    periodo = models.CharField('Período', max_length=30)
    fecha = models.DateField(auto_now_add=True)
    class Meta:
        constraints = [models.UniqueConstraint(fields=['estudiante','asignatura','periodo'], name='matricula_unica')]
    def __str__(self):
        return f'{self.estudiante} - {self.asignatura} ({self.periodo})'

class Calificacion(models.Model):
    matricula = models.OneToOneField(Matricula, on_delete=models.PROTECT)
    nota = models.DecimalField(max_digits=5, decimal_places=2, validators=[MinValueValidator(0),MaxValueValidator(100)])
    class Meta:
        constraints = [models.CheckConstraint(condition=models.Q(nota__gte=0, nota__lte=100), name='nota_valida')]
    def __str__(self):
        return f'{self.matricula}: {self.nota}'
