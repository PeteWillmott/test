from django.shortcuts import render, redirect, reverse
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from .forms import UserLoginForm, UserRegistrationForm

# Create your views here.
def index(request):
    """Return the index.html file."""

    return render(request, 'index.html')


@login_required
def login(request):
    """Log in user."""
    login_form = UserLoginForm()

    return render(request, 'login.html', {"login_form": login_form})


def logout(request):
    """Logout user."""
    auth.logout(request)
    messages.success(request, "You have successfully been logged out")

    return redirect(reverse('index'))


def register(request):
    """Register a new user."""
    if request.user.is_authenticated:
        return redirect(reverse('index'))

    if request.method == "POST":
        registration_form = UserRegistrationForm(request.POST)

        if registration_form.is_valid():
            registration_form.save()

            user = auth.authenticate(username=request.POST['username'],
                                        password=request.POST['password1'])
            if user:
                auth.login(user=user, request=request)
                messages.success(request, "You have successfully registered")
                return render(request, 'index.html')
            else:
                messages.error(request, "Unable to register your account at this time")
    else:
        registration_form = UserRegistrationForm()

    return render(request, 'register.html', {"registration_form": registration_form})

