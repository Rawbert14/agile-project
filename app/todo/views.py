from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from todo.models import Task

@login_required
def addTask(request):
    task_text = request.POST['task']
    Task.objects.create(task=task_text, created_by=request.user)
    return redirect('todo')

@login_required
def mark_as_done(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.status = Task.DONE
    task.done_by = request.user
    task.save()
    return redirect('todo')

@login_required
def mark_as_in_progress(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.status = Task.IN_PROGRESS
    task.in_progress_by = request.user
    task.save()
    return redirect('todo')

@login_required
def mark_as_undone(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.status = Task.TODO
    task.save()
    return redirect('todo')

@login_required
def edit_task(request, pk):
    get_task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        new_task = request.POST['task']
        get_task.task = new_task
        get_task.save()
        return redirect('todo')
    else:
        context = {'get_task': get_task}
        return render(request, 'edit_task.html', context)

@login_required
def delete_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect('todo')

@login_required
def mark_as_done_from_in_progress(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.status = Task.DONE
    task.done_by = request.user
    task.save()
    return redirect('todo')
