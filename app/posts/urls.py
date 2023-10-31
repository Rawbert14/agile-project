from django.urls import path
from .views import PostCreateView


app_name = 'posts'

urlpatterns = [
    path('board/', PostCreateView.as_view(), name='post-list')
]
