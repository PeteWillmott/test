from django.shortcuts import render, redirect, reverse
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from .forms import UserLoginForm, UserRegistrationForm
from catalogue.models import Catalogue


def login(request):
    """Return a login page."""

    if request.user.is_authenticated:
        return redirect(reverse('home:index'))
    if request.method == "POST":
        login_form = UserLoginForm(request.POST)

        if login_form.is_valid():
            user = auth.authenticate(username=request.POST['username'], password=request.POST['password'])
            
            if user:
                auth.login(user=user, request=request)
                messages.success(request, "You have logged in")
                return redirect(reverse('home:index'))
            else:
                login_form.add_error(None, "Your login credentials were not recognised.")
    else:
        login_form = UserLoginForm()
    return render(request, 'login.html', {"login_form": login_form})


@login_required(login_url='/login/')
def logout(request):
    """Logout user. Prevents unlogged in users logging out."""
    auth.logout(request)
    messages.success(request, "You have successfully been logged out")

    return redirect(reverse('home:index'))


def register(request):
    """Register a new user."""
    if request.user.is_authenticated:

        return redirect(reverse('home:index'))

    if request.method == "POST":
        registration_form = UserRegistrationForm(request.POST)
        if registration_form.is_valid():
            registration_form.save()

            user = auth.authenticate(username=request.POST['username'],
                                        password=request.POST['password1'])
            if user:
                auth.login(user=user, request=request)
                first_name = registration_form.cleaned_data.get('first_name')
                last_name = registration_form.cleaned_data.get('last_name')
                messages.success(request, f'Account created for {first_name} {last_name}.')
                return redirect(reverse('home:index'))
            else:
                messages.error(request, "Unable to register your account at this time")
    else:
        registration_form = UserRegistrationForm()

    return render(request, 'register.html', {"registration_form": registration_form})

