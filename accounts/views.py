from django.shortcuts import render, redirect, reverse
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from .forms import UserLoginForm, UserRegistrationForm, CustomerForm
from catalogue.models import Catalogue

# Create your views here.
def login(request):
    """Log in user."""
    login_form = UserLoginForm()

    return render(request, 'login.html', {"login_form": login_form})


@login_required
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
        customer_form = CustomerForm(request.POST)
        if registration_form.is_valid() and customer_form.is_valid():
            registration_form.save()
            customer_form.save()

            user = auth.authenticate(username=request.POST['username'],
                                        password=request.POST['password1'])
            if user:
                auth.login(user=user, request=request)
                title = registration_form.cleaned_data.get('title')
                first_name = registration_form.cleaned_data.get('first_name')
                last_name = registration_form.cleaned_data.get('last_name')
                messages.success(request, f'Account created for {title} {first_name} {last_name}.')
                return render(request, 'index.html')
            else:
                messages.error(request, "Unable to register your account at this time")
    else:
        registration_form = UserRegistrationForm()
        customer_form = CustomerForm()

    return render(request, 'register.html', {"customer_form":customer_form , "registration_form": registration_form})

