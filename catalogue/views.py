from django.shortcuts import render
from .models import Catalogue

# Create your views here.

def view_all(request):
    catalogue = Catalogue.objects.all()
    return render(request, 'display-all.html', {"catalogue": catalogue})


def view_one(request, id):
    display = Catalogue.objects.get(pk=id)
    return render(request, 'display-one.html', {"display": display})