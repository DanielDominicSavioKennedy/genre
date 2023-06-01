from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('home/',views.classify,name="home"),
    path('classify/',views.classify,name="classify"),
]
