from django.http import HttpResponse
from django.shortcuts import render

from blogs.models import Category, Blog
from todo.models import Task


def home(request):
    categories = Category.objects.all()
    posts = Blog.objects.filter(status='Published').order_by('updated_at')
    context = {
        'categories': categories,
        'posts': posts,
    }
    return render(request, 'home.html', context)

def todo(request):
    tasks = Task.objects.filter(is_completed=False).order_by('-updated_at')
    #print(tasks)
    completed_tasks = Task.objects.filter(is_completed=True).order_by('-updated_at')
    context = {
        'tasks': tasks,
        'completed_tasks': completed_tasks
    }
    return render(request, 'todo.html', context)

def help(request):
    return render(request, 'help.html')