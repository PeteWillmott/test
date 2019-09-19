from django.urls import path, include
from . import views
from .models import Catalogue
#from bid.forms import BidForm

app_name = 'catalogue'
urlpatterns = [
    path('', views.view_all, name="catalogue-all"),
    path('<int:pk>', views.view_one, name="catalogue-one"),
]