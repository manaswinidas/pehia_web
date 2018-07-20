from django.contrib import admin
from django.urls import path, include
from . import views
from django.urls import re_path

urlpatterns = [
    path('', views.index, name= 'index'),
    path('dashboard', views.dashboard, name= 'dashboard'),
    re_path(r'^', include('django.contrib.auth.urls')),
    re_path(r'^', include('social_django.urls')),
]
