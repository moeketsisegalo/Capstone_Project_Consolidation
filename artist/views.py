# Importing necessary modules and models
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import Album, Tour

# Home page view
def home(request):
    return render(request, 'home.html')

# Albums page view
def albums(request):
    # Retrieving all album objects from database
    albums = Album.objects.all()
    return render(request, 'albums.html', {'albums': albums})

# Tours page view
def tour(request):
    # Retrieving all tour objects from database
    tours = Tour.objects.all()
    return render(request, 'tours.html', {'tours': tours})

# User registration view
def register(request):
    # Redirecting to home page if user is already authenticated
    if request.user.is_authenticated:
        return redirect('home')
    # Handling form submission for new user registration
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            # Authenticating the user and logging them in
            user = authenticate(request, username=username, password=password)
            login(request, user)
            # Displaying success message
            messages.success(request, f"Account created for {username}!")
            return redirect('home')
    else:
        # Displaying registration form
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

# User login view
def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        # Authenticating the user
        user = authenticate(request, username=username, password=password)
        if user is not None:
            # Logging the user in and redirecting to home page
            login(request, user)
            return redirect('home')
        else:
            # Displaying error message for incorrect login credentials
            error_message = 'Incorrect username or password. Please try again.'
            return render(request, 'login.html', {'form': AuthenticationForm(), 'error_message': error_message})
    else:
        # Displaying login form
        return render(request, 'login.html', {'form': AuthenticationForm()})
