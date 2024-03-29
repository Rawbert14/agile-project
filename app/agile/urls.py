"""
URL configuration for agile project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views
from blogs import views as BlogsView
from quiz import views as QuizViews


urlpatterns = [
    path("admin/", admin.site.urls),
    #path('quiz/', QuizViews.quiz, name='quiz'),
    #path('quiz/', include('quiz.urls', namespace='quiz')),
    path('quiz/', include('quiz.urls', namespace='quiz')),
    path('quizcat/', QuizViews.home, name='quiz_home'),
    path('todo/', views.todo, name='todo'),
    path('help/', views.help, name='help'),
    path('policy/', views.policy, name='policy'),
    path('social/', views.social, name='social'),
    path('team/', views.team, name='team'),
    path("profile/", include('profiles.urls', namespace='profiles')),
    path('', include('reports.urls', namespace='reports')),
    path('posts/', include('posts.urls', namespace='posts')),
    path('accounts/', include('allauth.urls')),
    path('learning/', views.home, name='home'),
    path('<slug:slug>/', BlogsView.blogs, name='blogs'),
    path('category/<int:category_id>/', BlogsView.posts_by_category, name='posts_by_category'),
    path('todos/', include('todo.urls')),    
    
]

urlpatterns += static(
    settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += static(
    settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
