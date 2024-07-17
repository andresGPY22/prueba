from django.shortcuts import render, get_object_or_404, redirect
from .models import Estudiante, Asignatura, Calificacion
from django.db.models import Avg
from .forms import *



def registrar_calificacion(request, estudiante_id):
    estudiante = get_object_or_404(Estudiante, id=estudiante_id)
    asignaturas = Asignatura.objects.all()

    if request.method == 'POST':
        asignatura_id = request.POST['asignatura']
        tipo = request.POST['tipo']
        valor = request.POST['valor']
        asignatura = get_object_or_404(Asignatura, id=asignatura_id)
        Calificacion.objects.create(estudiante=estudiante, asignatura=asignatura, tipo=tipo, valor=valor)
        return redirect('listar_estudiantes')

    return render(request, 'gestion/registrar_calificacion.html', {'estudiante': estudiante, 'asignaturas': asignaturas})
def lista_docentes(request):
    docentes = Docente.objects.all()
    return render(request, 'lista_docentes.html', {'docentes': docentes})

def crear_docente(request):
    if request.method == 'POST':
        form = DocenteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_docentes')
    else:
        form = DocenteForm()
    return render(request, 'crear_docente.html', {'form': form})

def lista_estudiantes(request):
    estudiantes = Estudiante.objects.all()
    return render(request, 'lista_estudiantes.html', {'estudiantes': estudiantes})

def crear_estudiante(request):
    if request.method == 'POST':
        form = EstudianteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_estudiantes')
    else:
        form = EstudianteForm()
    return render(request, 'crear_estudiante.html', {'form': form})

def lista_calificaciones(request):
    calificaciones = Calificacion.objects.all()
    return render(request, 'lista_calificaciones.html', {'calificaciones': calificaciones})

def crear_calificacion(request):
    if request.method == 'POST':
        form = CalificacionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_calificaciones')
    else:
        form = CalificacionForm()
    return render(request, 'crear_calificacion.html', {'form': form})
def calcular_promedios(request):
    estudiantes = Estudiante.objects.all()
    resultados = []

    for estudiante in estudiantes:
        promedio = Calificacion.objects.filter(estudiante=estudiante).aggregate(Avg('valor'))['valor__avg']
        estado = 'Aprobado' if promedio and promedio >= 7 else 'Reprobado'
        resultados.append({'estudiante': estudiante, 'promedio': promedio, 'estado': estado})

    return render(request, 'gestion/calcular_promedios.html', {'resultados': resultados})

def filtrar_estudiantes(request, estado):
    estudiantes = Estudiante.objects.all()
    resultados = []

    for estudiante in estudiantes:
        promedio = Calificacion.objects.filter(estudiante=estudiante).aggregate(Avg('valor'))['valor__avg']
        if (estado == 'aprobado' and promedio and promedio >= 7) or (estado == 'reprobado' and (promedio is None or promedio < 7)):
            resultados.append(estudiante)

    return render(request, 'gestion/filtrar_estudiantes.html', {'estudiantes': resultados, 'estado': estado})
