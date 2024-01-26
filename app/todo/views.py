from django.forms import ValidationError
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from todo.models import Task
from django.contrib.auth.models import User
from django.contrib import messages  # Import messages

@login_required
def addTask(request):
    if request.method == 'POST':
        task_text = request.POST.get('task', '').strip()  # Use strip() to remove leading/trailing whitespace
        if not task_text:
            messages.error(request, "Task cannot be empty.")  # Add an error message
            return redirect('todo')  # Redirect back to the task form

        assigned_to_user = request.POST.get('assigned_to')
        assigned_to = User.objects.get(id=assigned_to_user) if assigned_to_user else None
        Task.objects.create(task=task_text, created_by=request.user, assigned_to=assigned_to)
        messages.success(request, "Task added successfully.")  # Optional success message
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
    task = get_object_or_404(Task, pk=pk)
    users = User.objects.all()

    if request.method == 'POST':
        try:
            task_text = request.POST.get('task', '').strip()
            if not task_text:
                raise ValidationError("Task text cannot be empty.")

            assigned_to_user = request.POST.get('assigned_to')
            assigned_to = User.objects.filter(id=assigned_to_user).first()

            task.task = task_text
            task.assigned_to = assigned_to
            task.save()

            return redirect('todo')
        except ValidationError as e:
            # Handle validation errors
            context = {'task': task, 'error': e.message}
            return render(request, 'edit_task.html', context)

    else:
        context = {'task': task, 'users':users}
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
