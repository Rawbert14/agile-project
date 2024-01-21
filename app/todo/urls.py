from django.urls import path
from . import views

urlpatterns = [
    path('addTask/', views.addTask, name='addTask'),
    path('mark_as_done/<int:pk>/', views.mark_as_done, name='mark_as_done'),
    path('mark_as_undone/<int:pk>/', views.mark_as_undone, name='mark_as_undone'),
    path('edit_task/<int:pk>/', views.edit_task, name='edit_task'),
    path('delete_task/<int:pk>/', views.delete_task, name='delete_task'),
    path('mark_as_in_progress/<int:pk>/', views.mark_as_in_progress, name='mark_as_in_progress'),
    path('mark_as_done_from_in_progress/<int:pk>/', views.mark_as_done_from_in_progress, name='mark_as_done_from_in_progress'),
    

]
