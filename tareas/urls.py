from django.urls import path
from .views import tareas, crear_tarea, detalle_tarea

urlpatterns = [
    path("tareas/", tareas, name="tareas"),
    path("crear_tarea/",crear_tarea, name="crear_tarea"),
    path("detalle_tarea/<int:asd>/", detalle_tarea, name="detalle_tarea")
]
