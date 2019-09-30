from django.urls import path, include
from .views import view_all, view_era, view_one
from .models import Catalogue

app_name = 'catalogue'
urlpatterns = [
    path('', view_all, name="catalogue-all"),
    path('<int:pk>', view_one, name="catalogue-one"),
    path('era', view_era, name="catalogue-era"),
]