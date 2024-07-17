from django.urls import path
from . import views

urlpatterns = [
    path('estudiantes/', views.lista_estudiantes, name='listar_estudiantes'),
    path('calificacion/<int:estudiante_id>/', views.registrar_calificacion, name='registrar_calificacion'),
    path('promedios/', views.calcular_promedios, name='calcular_promedios'),
    path('filtrar/<str:estado>/', views.filtrar_estudiantes, name='filtrar_estudiantes'),
    path('docentes/crear/', views.crear_docente, name='crear_docente'),
    path('estudiantes/crear/', views.crear_estudiante, name='crear_estudiante'),
    path('calificaciones/crear/', views.crear_calificacion, name='crear_calificacion'),
]

