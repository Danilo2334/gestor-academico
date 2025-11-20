from django.contrib import admin
from .models import (
    Perfil,
    Estudiante,
    Docente,
    Curso,
    Materia,
    Matricula,
    Calificacion,
    Asistencia,
)


@admin.register(Perfil)
class PerfilAdmin(admin.ModelAdmin):
    list_display = ("user", "rol", "activo")
    list_filter = ("rol", "activo")
    search_fields = ("user__username", "user__first_name", "user__last_name")


@admin.register(Estudiante)
class EstudianteAdmin(admin.ModelAdmin):
    list_display = ("user", "documento", "telefono")
    search_fields = ("user__username", "documento", "user__first_name", "user__last_name")


@admin.register(Docente)
class DocenteAdmin(admin.ModelAdmin):
    list_display = ("user", "titulo", "telefono")
    search_fields = ("user__username", "user__first_name", "user__last_name")


@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ("nombre", "codigo", "anio", "activo")
    list_filter = ("anio", "activo")
    search_fields = ("nombre", "codigo")


@admin.register(Materia)
class MateriaAdmin(admin.ModelAdmin):
    list_display = ("nombre", "codigo", "curso", "docente")
    list_filter = ("curso",)
    search_fields = ("nombre", "codigo")


@admin.register(Matricula)
class MatriculaAdmin(admin.ModelAdmin):
    list_display = ("estudiante", "curso", "fecha_matricula", "activo")
    list_filter = ("curso", "activo")


@admin.register(Calificacion)
class CalificacionAdmin(admin.ModelAdmin):
    list_display = ("estudiante", "materia", "periodo", "nota", "fecha_registro")
    list_filter = ("materia", "periodo")
    search_fields = ("estudiante__user__first_name", "estudiante__user__last_name")


@admin.register(Asistencia)
class AsistenciaAdmin(admin.ModelAdmin):
    list_display = ("estudiante", "materia", "fecha", "estado")
    list_filter = ("estado", "materia")
    search_fields = ("estudiante__user__first_name", "estudiante__user__last_name")
