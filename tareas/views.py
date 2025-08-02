from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import Formulario_Tarea
from django.urls import reverse
from .models import Tarea

# Create your views here.

@login_required
def tareas(request):
    tareas = Tarea.objects.filter(user=request.user)
    return render(request, "tareas.html", {"tareas": tareas})


def crear_tarea(request):
    if request.method == "GET":
        return render(request, "crear_tarea.html", {"form": Formulario_Tarea})
    else:
        form = Formulario_Tarea(request.POST)
        nueva_tarea = form.save(commit=False)
        nueva_tarea.user = request.user
        nueva_tarea.save()
        return redirect("tareas")
        

def detalle_tarea(request, asd):
    tarea = Tarea.objects.get(pk=asd)
    form = Formulario_Tarea(instance=tarea)
    return render(request, "detalle_tarea.html", {"tarea":tarea, "form":form})
