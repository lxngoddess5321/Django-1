from django.urls import path
from django.shortcuts import render_to_response
from . import views

app_name = 'items'
urlpatterns = [
    path('', views.index,name='index'),
]