from django.shortcuts import render, redirect

from .models import Blog, Post
from .forms import BlogForm, PostForm

def homepage(request):
    """The home page for Blogs."""
    return render(request, 'blogs/homepage.html')

def blogs(request):
    """Show all blogs."""
    blogs = Blog.objects.order_by('date_added')
    context = {'blogs': blogs}
    return render(request, 'blogs/blogs.html', context)

def blog(request, blog_id):
    """Show a certain blog's posts."""
    blog = Blog.objects.get(id=blog_id)
    posts = blog.post_set.order_by('date_added')
    context = {'blog': blog, 'posts': posts}
    return render(request, 'blogs/blog.html', context)

def new_blog(request):
    """Add a new blog."""
    if request.method != 'POST':
        # no data sumbitted, so create a blank form
        form = BlogForm()
    else:
        # data sumbitted, so process the data
        form = BlogForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('blogs:blogs')
    
    context = {'form': form}
    return render(request, 'blogs/new_blog.html', context)

def new_post(request, blog_id):
    """Add a new post."""
    blog = Blog.objects.get(id=blog_id)

    if request.method != 'POST':
        # Create a blank form
        form = PostForm()
    else:
        # Process the data
        form = PostForm(data=request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.blog = blog
            new_post.save()
            return redirect('blogs:blog', blog_id=blog_id)
    
    context = {'blog':blog, 'form': form}
    return render(request, 'blogs/new_post.html', context)

def edit_post(request, post_id):
    """Edit a post."""
    post = Post.objects.get(id=post_id)
    blog = post.blog

    if request.method != 'POST':
        # fill form with existing data
        form = PostForm(instance=post)
    else:
        # Porcess the data
        form = PostForm(instance=post, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('blogs:blog', blog_id=blog.id)
    
    context = {'blog': blog, 'post': post, 'form': form}
    return render(request, 'blogs/edit_post.html', context)