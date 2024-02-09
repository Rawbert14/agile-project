from django.forms import ValidationError
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from todo.models import Task
from django.contrib.auth.models import User
from django.contrib import messages  

from django.core.exceptions import ValidationError
from django.utils.dateparse import parse_date

from django.db.models import Sum
from django.contrib.auth.decorators import login_required
from .models import Task


def addTask(request):
    if request.method == 'POST':
        task_text = request.POST.get('task', '').strip()
        if not task_text:
            messages.error(request, "Task cannot be empty.")
            return redirect('todo')  # Adjust the redirect as needed

        # Handling the assignment of the task to a user
        assigned_to_user = request.POST.get('assigned_to')
        assigned_to = User.objects.get(id=assigned_to_user) if assigned_to_user else None

        # Handling the deadline
        deadline_text = request.POST.get('deadline')
        deadline = None
        if deadline_text:
            try:
                deadline = parse_date(deadline_text)
                if not deadline:
                    raise ValidationError("Invalid date format. It must be in YYYY-MM-DD format.")
            except ValidationError as e:
                messages.error(request, str(e))
                return redirect('todo')  # Adjust the redirect as needed

        # Handling the urgency
        urgency = request.POST.get('urgency', Task.LOW)

        # Handling the description
        description = request.POST.get('description', '').strip()  # Getting the description, defaulting to an empty string if not provided

        # Handling the expected time in minutes
        expected_time = request.POST.get('expected_time', '0').strip()
        try:
            expected_time = int(expected_time)
        except ValueError:
            expected_time = 0  # Default to 0 if conversion fails

        # Creating the task with all the provided information
        Task.objects.create(
            task=task_text,
            urgency=urgency,
            deadline=deadline,
            created_by=request.user,
            assigned_to=assigned_to,
            description=description,
            expected_time=expected_time
        )

        messages.success(request, "Task added successfully.")
        
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
        task_text = request.POST.get('task', '').strip()
        if not task_text:
            messages.error(request, "Task text cannot be empty.")
            return redirect('edit_task', pk=task.pk)  # Redirect back to the edit page

        assigned_to_user = request.POST.get('assigned_to')
        assigned_to = User.objects.filter(id=assigned_to_user).first() if assigned_to_user else None

        deadline_text = request.POST.get('deadline')
        deadline = parse_date(deadline_text) if deadline_text else None

        description = request.POST.get('description', '').strip()
        expected_time_text = request.POST.get('expected_time', '0').strip()
        try:
            expected_time = int(expected_time_text)
        except ValueError:
            expected_time = 0  # Default to 0 if conversion fails

        task.task = task_text
        task.assigned_to = assigned_to
        task.deadline = deadline
        task.urgency = request.POST.get('urgency', Task.LOW)
        task.description = description
        task.expected_time = expected_time
        task.save()

        messages.success(request, "Task updated successfully.")
        return redirect('todo')  # Adjust the redirect as needed

    context = {'task': task, 'users': users}
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