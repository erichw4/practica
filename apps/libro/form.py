from django import forms

from .models import Autor


class AutorForm(forms.ModelForm):  # herencias de modelForm
    class Meta:  # nos ahorra codigo de escribir
        model = Autor
        fields = ['nombre', 'apellidos', 'nacionalidad', 'descripcion']
