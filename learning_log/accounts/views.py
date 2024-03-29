from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

def register(request):
    """Register a new user."""
    if request.method != 'POST':
        # Display a blank registration form.
        form = UserCreationForm()
    else:
        # Process the completed form.
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            # Log in the user and then redirect to the homepage.
            login(request, new_user)
            return redirect('learning_logs:index')
    
    # Display a blank or invalid form.
    context = {'form': form}
    return render(request, 'registration/register.html', context)