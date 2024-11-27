from django import forms
from .models import Ambiente, Camada


class AmbienteForm(forms.ModelForm):
    class Meta:
        model = Ambiente
        fields = '__all__'


class CamadaForm(forms.ModelForm):
    class Meta:
        model = Camada
        fields = '__all__'
