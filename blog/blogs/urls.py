"""Defines URL patterns for Blogs."""

from django.urls import path

from . import views

app_name = 'blogs'
urlpatterns = [
    # Home page
    path('', views.homepage, name='homepage'),

    # Page that shows all blogs
    path('blogs/', views.blogs, name='blogs'),

    # Page that shows a certain blog's posts
    path('blogs/<int:blog_id>/', views.blog, name='blog'),

    # Page for adding a new blog
    path('new_blog/', views.new_blog, name='new_blog'),

    # Page for adding a new post
    path('new_post/<int:blog_id>/', views.new_post, name='new_post'),

    # Page for editing an entry
    path('edit_post/<int:post_id>/', views.edit_post, name='edit_post'),
]