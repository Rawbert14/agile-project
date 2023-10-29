from django.urls import path
from .views import test_view, test_view_2

app_name = 'profiles'

urlpatterns = [
    path('', test_view, name='test-view-1'),
    path('view3/', test_view_2, name='test-view-2'),
]


