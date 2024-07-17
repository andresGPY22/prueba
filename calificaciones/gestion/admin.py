from django.contrib import admin
from .models import Docente, Estudiante, Calificacion

admin.site.register(Docente)
admin.site.register(Estudiante)
admin.site.register(Calificacion)

# Register your models here.
