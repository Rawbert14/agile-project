from django.http import HttpResponse
from django.shortcuts import render

from blogs.models import Category, Blog


def home(request):
    categories = Category.objects.all()
    posts = Blog.objects.filter(status='Published').order_by('updated_at')
    context = {
        'categories': categories,
        'posts': posts,
    }
    return render(request, 'home.html', context)