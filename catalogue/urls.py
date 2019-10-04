from django.urls import path, include
from django.conf.urls import url, include
from .views import view_all, view_era, view_one
from .models import Catalogue

app_name = 'catalogue'
urlpatterns = [      
    url(r'^$', view_all, name="catalogue-all"),      
    url(r'^era(\d+)', view_era, name='view_era'),      
    url(r'^item/(\d+)', view_one, name="catalogue-one")
] 