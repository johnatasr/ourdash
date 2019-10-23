from django.urls import path
from .views import index

app_name = 'portal'

urlpatterns = [
    path('', index, name='home'),
]
