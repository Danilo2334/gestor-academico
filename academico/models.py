from django.db import models
from django.contrib.auth.models import User


class Perfil(models.Model):
    ROLE_CHOICES = [
        ("ADMIN", "Administrador"),
        ("DOCENTE", "Docente"),
        ("ESTUDIANTE", "Estudiante"),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="perfil")
    rol = models.CharField(max_length=20, choices=ROLE_CHOICES, default="ESTUDIANTE")
    activo = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.user.username} ({self.get_rol_display()})"


class Estudiante(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="estudiante")
    documento = models.CharField(max_length=20, unique=True)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    telefono = models.CharField(max_length=20, blank=True)
    direccion = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return f"{self.user.get_full_name()} - {self.documento}"


class Docente(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="docente")
    titulo = models.CharField(max_length=100, blank=True)
    telefono = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.user.get_full_name() or self.user.username


class Curso(models.Model):
    nombre = models.CharField(max_length=100)
    codigo = models.CharField(max_length=20, unique=True)
    anio = models.IntegerField()
    activo = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.nombre} ({self.codigo})"


class Materia(models.Model):
    nombre = models.CharField(max_length=100)
    codigo = models.CharField(max_length=20, unique=True)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, related_name="materias")
    docente = models.ForeignKey(Docente, on_delete=models.SET_NULL, null=True, blank=True, related_name="materias")

    def __str__(self):
        return f"{self.nombre} - {self.curso.nombre}"


class Matricula(models.Model):
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE, related_name="matriculas")
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, related_name="matriculas")
    fecha_matricula = models.DateField(auto_now_add=True)
    activo = models.BooleanField(default=True)

    class Meta:
        unique_together = ("estudiante", "curso")

    def __str__(self):
        return f"{self.estudiante} en {self.curso}"


class Calificacion(models.Model):
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE, related_name="calificaciones")
    materia = models.ForeignKey(Materia, on_delete=models.CASCADE, related_name="calificaciones")
    docente = models.ForeignKey(Docente, on_delete=models.SET_NULL, null=True, blank=True, related_name="calificaciones")
    periodo = models.CharField(max_length=20, default="1")
    nota = models.DecimalField(max_digits=4, decimal_places=2)  # 0.00 - 10.00
    fecha_registro = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("estudiante", "materia", "periodo")

    def __str__(self):
        return f"{self.estudiante} - {self.materia} - {self.nota}"


class Asistencia(models.Model):
    ESTADO_CHOICES = [
        ("P", "Presente"),
        ("A", "Ausente"),
        ("T", "Tarde"),
        ("J", "Justificado"),
    ]

    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE, related_name="asistencias")
    materia = models.ForeignKey(Materia, on_delete=models.CASCADE, related_name="asistencias")
    fecha = models.DateField()
    estado = models.CharField(max_length=1, choices=ESTADO_CHOICES, default="P")

    class Meta:
        unique_together = ("estudiante", "materia", "fecha")

    def __str__(self):
        return f"{self.estudiante} - {self.materia} - {self.fecha} - {self.estado}"
