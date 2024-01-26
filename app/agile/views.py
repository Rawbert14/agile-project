from django.http import HttpResponse
from django.shortcuts import render

from blogs.models import Category, Blog
from todo.models import Task
from profiles.models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


def home(request):
    categories = Category.objects.all()
    posts = Blog.objects.filter(status='Published').order_by('updated_at')
    context = {
        'categories': categories,
        'posts': posts,
    }
    return render(request, 'home.html', context)


@login_required
def todo(request):
    tasks = Task.objects.filter(status=Task.TODO).order_by('-updated_at')
    in_progress_tasks = Task.objects.filter(status=Task.IN_PROGRESS).order_by('-updated_at')
    completed_tasks = Task.objects.filter(status=Task.DONE).order_by('-updated_at')
    
    # Get tasks assigned to the logged-in user
    assigned_tasks = Task.objects.filter(assigned_to=request.user).order_by('-updated_at')

    context = {
        'tasks': tasks,
        'in_progress_tasks': in_progress_tasks,
        'completed_tasks': completed_tasks,
        'assigned_tasks': assigned_tasks,  # Add this line
    }
    return render(request, 'todo.html', context)


def help(request):
    return render(request, 'help.html')

def team(request):
    members = Profile.objects.all()
    context = {
        'members': members,
    }
    return render(request, 'team.html', context)

def social(request):
    return render(request, 'social.html')

def policy(request):
    return render(request, 'policy.html')