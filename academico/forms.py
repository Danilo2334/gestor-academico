from django import forms
from django.contrib.auth.models import User

from .models import (
    Estudiante,
    Docente,
    Curso,
    Materia,
    Calificacion,
    Asistencia,
    Perfil,
)


# ========= Estudiante =========


class EstudianteForm(forms.ModelForm):
    username = forms.CharField(max_length=150, label="Usuario")
    first_name = forms.CharField(max_length=150, label="Nombres")
    last_name = forms.CharField(max_length=150, label="Apellidos")
    email = forms.EmailField(label="Correo")

    class Meta:
        model = Estudiante
        fields = ["documento", "fecha_nacimiento", "telefono", "direccion"]

    def __init__(self, *args, **kwargs):
        self.user_instance = kwargs.pop("user_instance", None)
        super().__init__(*args, **kwargs)
        if self.instance and self.instance.pk:
            self.fields["username"].initial = self.instance.user.username
            self.fields["first_name"].initial = self.instance.user.first_name
            self.fields["last_name"].initial = self.instance.user.last_name
            self.fields["email"].initial = self.instance.user.email

    def save(self, commit=True):
        if self.user_instance is None:
            user = User(
                username=self.cleaned_data["username"],
                first_name=self.cleaned_data["first_name"],
                last_name=self.cleaned_data["last_name"],
                email=self.cleaned_data["email"],
            )
            user.set_password("123456")  # contrasena por defecto
            if commit:
                user.save()
        else:
            user = self.user_instance
            user.username = self.cleaned_data["username"]
            user.first_name = self.cleaned_data["first_name"]
            user.last_name = self.cleaned_data["last_name"]
            user.email = self.cleaned_data["email"]
            if commit:
                user.save()

        estudiante = super().save(commit=False)
        estudiante.user = user
        if commit:
            estudiante.save()
            perfil, _ = Perfil.objects.get_or_create(user=user)
            perfil.rol = "ESTUDIANTE"
            perfil.activo = True
            perfil.save()
        return estudiante


# ========= Docente =========


class DocenteForm(forms.ModelForm):
    username = forms.CharField(max_length=150, label="Usuario")
    first_name = forms.CharField(max_length=150, label="Nombres")
    last_name = forms.CharField(max_length=150, label="Apellidos")
    email = forms.EmailField(label="Correo")

    class Meta:
        model = Docente
        fields = ["titulo", "telefono"]

    def __init__(self, *args, **kwargs):
        self.user_instance = kwargs.pop("user_instance", None)
        super().__init__(*args, **kwargs)
        if self.instance and self.instance.pk:
            self.fields["username"].initial = self.instance.user.username
            self.fields["first_name"].initial = self.instance.user.first_name
            self.fields["last_name"].initial = self.instance.user.last_name
            self.fields["email"].initial = self.instance.user.email

    def save(self, commit=True):
        if self.user_instance is None:
            user = User(
                username=self.cleaned_data["username"],
                first_name=self.cleaned_data["first_name"],
                last_name=self.cleaned_data["last_name"],
                email=self.cleaned_data["email"],
            )
            user.set_password("123456")
            if commit:
                user.save()
        else:
            user = self.user_instance
            user.username = self.cleaned_data["username"]
            user.first_name = self.cleaned_data["first_name"]
            user.last_name = self.cleaned_data["last_name"]
            user.email = self.cleaned_data["email"]
            if commit:
                user.save()

        docente = super().save(commit=False)
        docente.user = user
        if commit:
            docente.save()
            perfil, _ = Perfil.objects.get_or_create(user=user)
            perfil.rol = "DOCENTE"
            perfil.activo = True
            perfil.save()
        return docente


# ========= Curso =========


class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = ["nombre", "codigo", "anio", "activo"]


# ========= Materia =========


class MateriaForm(forms.ModelForm):
    class Meta:
        model = Materia
        fields = ["nombre", "codigo", "curso", "docente"]


# ========= Calificacion =========


class CalificacionForm(forms.ModelForm):
    class Meta:
        model = Calificacion
        fields = ["estudiante", "materia", "docente", "periodo", "nota"]

    def clean_nota(self):
        nota = self.cleaned_data["nota"]
        if nota < 0 or nota > 10:
            raise forms.ValidationError("La nota debe estar entre 0 y 10.")
        return nota


# ========= Asistencia =========


class AsistenciaForm(forms.ModelForm):
    class Meta:
        model = Asistencia
        fields = ["estudiante", "materia", "fecha", "estado"]
        widgets = {
            "fecha": forms.DateInput(attrs={"type": "date"}),
        }
