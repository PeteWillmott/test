from django.urls import path
from .views import index, login, logout, register
from catalogue.models import Catalogue

urlpatterns = [
    path('', index, name="index"),
    path('login', login, name="login"),
    path('logout', logout, name="logout"),
    path('register', register, name="register"),
]