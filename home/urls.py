from django.urls import path
from .views import index, about, contact, faq, how_to, shipping
from catalogue.models import Catalogue

app_name = 'home'
urlpatterns = [
    path('', index, name="index"),
    path('about', about, name="about"),
    path('contact', contact, name="contact"),
    path('FAQ', faq, name="faq"),
    path('how-to', how_to, name="how_to"),
    path('shipping', shipping, name="shipping"),
]