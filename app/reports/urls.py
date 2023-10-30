from django.urls import path
from .views import report_view, delete_view

app_name = 'reports'

urlpatterns = [
    path('<str:production_line>/', report_view, name="report-view"),
    path('delete/<pk>', delete_view, name='delete-view')
]
