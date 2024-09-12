from django import forms

from .models import Tarea


class TareaForm(forms.ModelForm):
    class Meta:
        model = Tarea  # Especificar el modelo al que pertenece el formulario
        fields = ['titulo', 'descripcion', 'completado']  # Indicar los campos que se incluirán en el formulario

