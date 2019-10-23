from django.urls import path
from .views import dashboard

app_name = 'dashboards'

urlpatterns = [
    path('teste/', dashboard, name='teste'),
]
