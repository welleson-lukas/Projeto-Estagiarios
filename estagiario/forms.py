from django import forms
from .models import Estagiario

class EstagiarioForm(forms.ModelForm):
    class Meta:
        model = Estagiario
        exclude = ('dt_cadastro', )
        fields = '__all__'
