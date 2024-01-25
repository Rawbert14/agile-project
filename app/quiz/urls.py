# quiz/urls.py
from django.urls import path
from . import views  # Import views from this app

urlpatterns = [
    path('home/', views.home, name='quiz_home'),  # The main quiz home view
    path('api/get-quiz/', views.get_quiz, name='get_quiz'),  # API endpoint
    path('', views.quiz, name='quiz'),  # The quiz view
    
]

