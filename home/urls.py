from django.urls import path
from .views import index, about, contact
from catalogue.models import Catalogue

app_name = 'home'
urlpatterns = [
    path('', index, name="index"),
    path('about', about, name="about"),
    path('contact', contact, name="contact"),
]