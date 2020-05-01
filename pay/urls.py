from django.urls import path
from django.shortcuts import render_to_response

from . import views

app_name = 'pay'
urlpatterns = [
    path('', views.index, name='success')
]
