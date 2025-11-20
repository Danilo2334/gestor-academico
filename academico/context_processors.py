from .models import Perfil


def perfil_usuario(request):
    perfil = None
    if request.user.is_authenticated:
        try:
            perfil = request.user.perfil
        except Perfil.DoesNotExist:
            perfil = None
    return {"perfil_usuario": perfil}
