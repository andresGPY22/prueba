from django import forms
from .models import Docente, Estudiante, Calificacion

class DocenteForm(forms.ModelForm):
    class Meta:
        model = Docente
        fields = '__all__'

class EstudianteForm(forms.ModelForm):
    class Meta:
        model = Estudiante
        fields = '__all__'

class CalificacionForm(forms.ModelForm):
    class Meta:
        model = Calificacion
        fields = '__all__'
