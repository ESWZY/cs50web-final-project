from django.urls import path

from . import views

urlpatterns = [
    path("", views.index),  # run func index in views.py
    path("second", views.second)
]
