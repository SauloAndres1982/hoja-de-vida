from django import forms
from . models import ProyectoDev

class ProyectoDevForm(forms.ModelForm):
    class Meta:
        model = ProyectoDev
        fields = ["name", "url", "tecnology", "description"]