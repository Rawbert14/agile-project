from django.urls import path
from .views import PostCreateView, like_post


app_name = 'posts'

urlpatterns = [
    path('board/', PostCreateView.as_view(), name='post-list'),
    path('like/', like_post, name='post-like')
]
