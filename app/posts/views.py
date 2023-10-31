from itertools import chain
from typing import Any
from django.shortcuts import render
from django.views.generic import CreateView
from .forms import PostForm
from django.urls import reverse_lazy
from .models import ProblemPost, GeneralPost
# Create your views here.

class PostCreateView(CreateView):
    form_class = PostForm
    template_name = 'posts/board.html'
    success_url = reverse_lazy('posts:post-list')
    
    def get_context_data(self, **kwargs):
        qs1 = ProblemPost.objects.public_only()
        qs2 = GeneralPost.objects.all()
        qs = sorted(chain(qs1, qs2), reverse=True, key=lambda obj: obj.created)
        context=super().get_context_data(**kwargs)
        context["object_list"]= qs
        return context
    