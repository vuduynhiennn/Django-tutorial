from urllib.parse import urlparse
from django.urls import path, include
from . import views

urlparses = [
    path('', views.home, name="home"),
    path('room/', views.room, name="room"),
]