
from django.contrib import admin
from django.urls import path
from tarea import views

urlpatterns = [
    path('', views.lista_tareas, name='lista_tareas'),
    path('crear/', views.crear_tarea, name='crear_tarea'),
    path ('detalle_tarea/<int:pk>', views.detalle_tarea, name='detalle_tarea') 
]
