from django.shortcuts import render, redirect, reverse
from .forms import UserLoginForm, UserRegistrationForm

# Create your views here.
def index(request):
    """Return the index.html file."""
    return render(request, 'index.html')


def login(request):
    """Log in user."""

    login_form = UserLoginForm()
    return render(request, 'login.html', {"login_form": login_form})


def register(request):
    """Register a new user."""

    registration_form = UserRegistrationForm()
    return render(request, 'register.html', {"registration_form": registration_form})

