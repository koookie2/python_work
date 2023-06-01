from django.shortcuts import render

def homepage(request):
    """The home page for Blogs."""
    return render(request, 'blogs/homepage.html')