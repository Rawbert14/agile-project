from django.urls import path
from .views import report_view

app_name = 'reports'

urlpatterns = [
    path('', report_view, name="report-view")
]
