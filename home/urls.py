from django.urls import path
from .views import index
from catalogue.models import Catalogue

urlpatterns = [
    path('', index, name="index"),
]