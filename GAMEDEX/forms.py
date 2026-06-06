from django import forms
from django.contrib.auth.models import User

class EditarPerfilForm(forms.ModelForm):
    password = forms.CharField(
        required=False,
        widget=forms.PasswordInput,
        label="Nueva contraseña"
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password']


# GAMEDEX/forms.py
from django import forms
from .models import Comunidad

class ComunidadForm(forms.ModelForm):
    class Meta:
        model = Comunidad
        fields = ['nombre', 'descripcion', 'imagen']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }
