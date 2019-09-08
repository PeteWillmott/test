from django.urls import path, include
from . import views
from .models import Catalogue

app_name = 'catalogue'
urlpatterns = [
    path('', views.view_all, name="catalogue-all"),
    #path('<int:pk>', view_one, name="catalogue-one"),
]