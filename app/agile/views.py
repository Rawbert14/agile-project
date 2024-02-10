from datetime import datetime
import random
from django.http import HttpResponse
from django.shortcuts import render
from areas.models import ProductionLine

from blogs.models import Category, Blog
from todo.models import Task
from profiles.models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from datetime import timedelta
from collections import defaultdict
from django.db.models import Sum
from django.contrib.auth.decorators import login_required

def home(request):
    categories = Category.objects.all()
    posts = Blog.objects.filter(status='Published').order_by('updated_at')
    #print(production_lines)

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
    users = User.objects.all() 
    today = timezone.localdate()
    five_days_later = today + timedelta(days=5)
    # Calculate total expected time for tasks assigned to the current user
    total_expected_time = Task.objects.filter(assigned_to=request.user).aggregate(Sum('expected_time'))['expected_time__sum'] or 0

    # Other context data
    tasks = Task.objects.filter(assigned_to=request.user)
    
    # Get tasks assigned to the logged-in user
    assigned_tasks = Task.objects.filter(assigned_to=request.user).order_by('-updated_at')

    context = {
        'tasks': tasks,
        'in_progress_tasks': in_progress_tasks,
        'completed_tasks': completed_tasks,
        'assigned_tasks': assigned_tasks,  
        'users': users,
        'today': today,
        'five_days_later': five_days_later,
        'total_expected_time': total_expected_time,
    }
    return render(request, 'todo.html', context)


def help(request):
    return render(request, 'help.html')

def team1(request):
    members = Profile.objects.all()
    context = {
        'members': members,
    }
    return render(request, 'team.html', context)


@login_required
def team(request):
    # Get the current week number
    current_week = datetime.now().isocalendar().week

    # Create a seed for the random number generator using the current week number
    seed = str(current_week)
    random.seed(seed)

    # Queryset excluding the current user to get the list of possible teammates
    teammates = Profile.objects.exclude(user=request.user)

    buddy = None
    # Check if there are any teammates
    if teammates.exists():
        # Get the count of teammates
        teammates_count = teammates.count()

        # Generate a random index from 0 to teammates_count - 1
        random_index = random.randint(0, teammates_count - 1)

        # Select the buddy using the random index
        buddy = teammates[random_index]

    context = {
        'buddy': buddy,
        'members': teammates, 
    }

    return render(request, 'team.html', context)




def social(request):
    return render(request, 'social.html')

def policy(request):
    return render(request, 'policy.html')
