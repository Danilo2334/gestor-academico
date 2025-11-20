from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings

from .models import Perfil, Calificacion, Docente, Estudiante


@receiver(post_save, sender=User)
def crear_perfil_usuario(sender, instance, created, **kwargs):
    if created:
        Perfil.objects.create(user=instance)


@receiver(post_save, sender=Calificacion)
def notificar_calificacion(sender, instance, created, **kwargs):
    estudiante = instance.estudiante
    correo = estudiante.user.email
    if correo:
        asunto = "Nueva calificación registrada"
        mensaje = (
            f"Hola {estudiante.user.get_full_name()},\n\n"
            f"Se ha registrado una nueva calificación:\n"
            f"Materia: {instance.materia.nombre}\n"
            f"Periodo: {instance.periodo}\n"
            f"Nota: {instance.nota}\n\n"
            f"Saludos,\nSistema de Gestión Académica"
        )
        send_mail(
            asunto,
            mensaje,
            settings.DEFAULT_FROM_EMAIL,
            [correo],
            fail_silently=True,
        )


@receiver(post_save, sender=Docente)
def actualizar_perfil_docente(sender, instance, **kwargs):
    perfil, _ = Perfil.objects.get_or_create(user=instance.user)
    perfil.rol = "DOCENTE"
    perfil.activo = True
    perfil.save()


@receiver(post_save, sender=Estudiante)
def actualizar_perfil_estudiante(sender, instance, **kwargs):
    perfil, _ = Perfil.objects.get_or_create(user=instance.user)
    perfil.rol = "ESTUDIANTE"
    perfil.activo = True
    perfil.save()
