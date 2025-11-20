from django.urls import path
from . import views

urlpatterns = [
    # Inicio / dashboard
    path("", views.inicio, name="inicio"),
    path("dashboard/", views.dashboard, name="dashboard"),
    # ===== ADMIN: Estudiantes =====
    path("estudiantes/", views.estudiante_list, name="estudiante_list"),
    path("estudiantes/nuevo/", views.estudiante_create, name="estudiante_create"),
    path("estudiantes/<int:pk>/editar/", views.estudiante_update, name="estudiante_update"),
    path("estudiantes/<int:pk>/eliminar/", views.estudiante_delete, name="estudiante_delete"),
    # ===== ADMIN: Docentes =====
    path("docentes/", views.docente_list, name="docente_list"),
    path("docentes/nuevo/", views.docente_create, name="docente_create"),
    path("docentes/<int:pk>/editar/", views.docente_update, name="docente_update"),
    path("docentes/<int:pk>/eliminar/", views.docente_delete, name="docente_delete"),
    # ===== ADMIN: Cursos =====
    path("cursos/", views.curso_list, name="curso_list"),
    path("cursos/nuevo/", views.curso_create, name="curso_create"),
    path("cursos/<int:pk>/editar/", views.curso_update, name="curso_update"),
    path("cursos/<int:pk>/eliminar/", views.curso_delete, name="curso_delete"),
    # ===== ADMIN: Materias =====
    path("materias/", views.materia_list, name="materia_list"),
    path("materias/nuevo/", views.materia_create, name="materia_create"),
    path("materias/<int:pk>/editar/", views.materia_update, name="materia_update"),
    path("materias/<int:pk>/eliminar/", views.materia_delete, name="materia_delete"),
    # ===== ADMIN: Calificaciones y Asistencia (CRUD general) =====
    path("calificaciones/", views.calificacion_list, name="calificacion_list"),
    path("calificaciones/nuevo/", views.calificacion_create, name="calificacion_create"),
    path("calificaciones/<int:pk>/editar/", views.calificacion_update, name="calificacion_update"),
    path("calificaciones/<int:pk>/eliminar/", views.calificacion_delete, name="calificacion_delete"),
    path("asistencias/", views.asistencia_list, name="asistencia_list"),
    path("asistencias/nueva/", views.asistencia_create, name="asistencia_create"),
    path("asistencias/<int:pk>/eliminar/", views.asistencia_delete, name="asistencia_delete"),
    path("asistencias/marcar/<int:materia_id>/", views.marcar_asistencia, name="marcar_asistencia"),
    # ===== DOCENTE: flujo propio =====
    path("docente/mis-materias/", views.docente_mis_materias, name="docente_mis_materias"),
    path(
        "docente/materia/<int:materia_id>/calificaciones/",
        views.docente_calificaciones_materia,
        name="docente_calificaciones_materia",
    ),
    # ===== ESTUDIANTE: flujo propio =====
    path("mi/calificaciones/", views.mis_calificaciones, name="mis_calificaciones"),
    path("mi/asistencia/", views.mi_asistencia, name="mi_asistencia"),
    path("mi/boletin/", views.mi_boletin, name="mi_boletin"),
    # ===== REPORTES (ADMIN / ESTUDIANTE) =====
    path("reportes/boletin/<int:estudiante_id>/", views.boletin_pdf, name="boletin_pdf"),
    path("reportes/calificaciones-excel/", views.calificaciones_excel, name="calificaciones_excel"),
    path("reportes/asistencia-excel/", views.asistencia_excel, name="asistencia_excel"),
]
