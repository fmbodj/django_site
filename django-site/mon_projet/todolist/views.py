from .forms import TaskForm
from django.shortcuts import render, redirect, get_object_or_404
from .models import Task


def task_list(request):
    # Initialisation des paramètres de tri et de filtrage
    sort_by = request.GET.get('sort', 'created_at')  # Tri par défaut par date de création
    status_filter = request.GET.get('status', None)  # Pas de filtre par défaut

    # Récupération des tâches avec filtrage optionnel
    if status_filter == 'done':
        tasks = Task.objects.filter(status=True)
    elif status_filter == 'todo':
        tasks = Task.objects.filter(status=False)
    else:
        tasks = Task.objects.all()

    # Application du tri
    tasks = tasks.order_by(sort_by)

    return render(request, 'todolist/task_list.html', {'tasks': tasks})

def task_add(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'todolist/task_form.html', {'form': form})

def task_edit(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)
    return render(request, 'todolist/task_form.html', {'form': form})

def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        task.delete()
        return redirect('task_list')
    return render(request, 'todolist/task_confirm_delete.html', {'task': task})
