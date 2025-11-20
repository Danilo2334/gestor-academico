from functools import wraps

from django.contrib import messages
from django.shortcuts import redirect


def rol_requerido(*roles_permitidos):
    """
    Verifica que el usuario tenga un Perfil con rol dentro de roles_permitidos
    y que esté activo. Si no cumple, lo redirige al dashboard.
    Superusuarios siempre se tratan como ADMIN.
    """

    def decorador(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            if not request.user.is_authenticated:
                return redirect("login")

            perfil = getattr(request.user, "perfil", None)

            if request.user.is_superuser:
                rol_usuario = "ADMIN"
                perfil_activo = True
            elif perfil is not None:
                rol_usuario = perfil.rol
                perfil_activo = perfil.activo
            else:
                rol_usuario = None
                perfil_activo = False

            if not perfil_activo or rol_usuario not in roles_permitidos:
                messages.error(request, "No tienes permiso para acceder a esta sección.")
                return redirect("dashboard")

            return view_func(request, *args, **kwargs)

        return _wrapped_view

    return decorador
