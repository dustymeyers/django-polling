from django.urls import path

# imports all functions from views.py
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]