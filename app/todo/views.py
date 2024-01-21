from django.shortcuts import get_object_or_404, redirect, render
from todo.models import Task

def addTask(request):
    task = request.POST['task']
    Task.objects.create(task=task)
    return redirect('todo')

def mark_as_done(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.status = Task.DONE
    task.save()
    return redirect('todo')

def mark_as_in_progress(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.status = Task.IN_PROGRESS
    task.save()
    return redirect('todo')

def mark_as_undone(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.status = Task.TODO
    task.save()
    return redirect('todo')

def edit_task(request, pk):
    get_task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        new_task = request.POST['task']
        get_task.task = new_task
        get_task.save()
        return redirect('todo')
    else:
        context = {
            'get_task': get_task,
        }
        return render(request, 'edit_task.html', context)

def delete_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect('todo')

def mark_as_done_from_in_progress(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.status = Task.DONE
    task.save()
    return redirect('todo')
