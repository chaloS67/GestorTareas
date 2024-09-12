
from email import message
from pyexpat.errors import messages
from django.shortcuts import get_object_or_404, redirect, render
from .models import Tarea
from .form import TareaForm
from .models import Tarea

# Create your views here.

def lista_tareas(request):

    tareas = Tarea.objects.all()
    return render (request,'tarea/lista_tareas.html',{'tareas': tareas})
    

def crear_tarea(request):
    if request.method == 'POST':
        form = TareaForm(request.POST)
        if form.is_valid():
            tarea = form.save()
           ## messages.success(request, 'Tarea creada exitosamente.')
            return redirect('detalle_tarea', pk=tarea.pk)  # Asegúrate de que esta URL esté definida
    else:
        form = TareaForm()  # Crear un formulario vacío para solicitudes GET

    return render(request, 'crear_tarea.html', {'form': form})

def detalle_tarea(request, pk):
    tarea = get_object_or_404(Tarea, pk=pk)
    return render(request, 'detalle_tarea.html',{'tarea': tarea})

def eliminar_tarea(request, pk):
    tarea = get_object_or_404(Tarea, pk=pk)
    tarea.delete()
    return redirect('lista_tareas')  # Redirige a la lista de tareas después de eliminar
    


