"""Defines URL patterns for Blogs."""

from django.urls import path

from . import views

app_name = 'blogs'
urlpatterns = [
    # Home page
    path('', views.homepage, name='index'),
]