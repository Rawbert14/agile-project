from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render

from .models import Blog, Category
from django.db.models import Q



def posts_by_category(request, category_id):
    posts = Blog.objects.filter(status='Published', category=category_id)
       
    category = get_object_or_404(Category, pk=category_id)
    
    context = {
        'posts': posts,
        'category': category,
    }
    return render(request, 'posts_by_category.html', context)


def blogs(request, slug):
    single_blog = get_object_or_404(Blog, slug=slug, status='Published')
    context =  {
        'single_blog': single_blog,
    }
    return render(request, 'blogs.html', context)