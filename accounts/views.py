from django.shortcuts import render, redirect, reverse
from .forms import UserLoginForm

# Create your views here.
def index(request):
    """Return the index.html file."""
    return render(request, 'index.html')

def login(request):
    """Log in user."""

    login_form = UserLoginForm()
    return render(request, 'login.html', {"login_form": login_form})

