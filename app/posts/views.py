from itertools import chain
from typing import Any
from django.shortcuts import redirect, render
from django.views.generic import CreateView
from .forms import PostForm
from django.urls import reverse_lazy
from .models import ProblemPost, GeneralPost
from profiles.models import Profile
from posts.models import Post, Like
from .mixins import FormUserRequiredMixin
# Create your views here.

class PostCreateView(FormUserRequiredMixin, CreateView):
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
    
def like_post(request):
    user = request.user
    profile = Profile.objects.get(user=user)
    if request.method=='POST':
        post_id = request.POST.get('post_id')
        post_obj = Post.objects.get(id=post_id)
        if profile in post_obj.liked.all():
            post_obj.liked.remove(profile)
        else:
            post_obj.liked.add(profile)
    like, created = Like.objects.get_or_create(user=profile, post_id=post_id)
    if not created:
        if like.value == 'Like':
            like.value = 'Unlike'
        else:
            like.value = 'Like'
    like.save()
    return redirect('posts:post-list')
        
    
        
    