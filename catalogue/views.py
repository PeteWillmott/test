from django.shortcuts import render, get_object_or_404
from .models import Catalogue
from .forms import CatalogueForm

def view_all(request):
    catalogue = Catalogue.objects.all()
    newest = Catalogue.objects.last()
    return render(request, 'display-all.html', {"catalogue": catalogue, "newest": newest})


def view_one(request, id):
    display = Catalogue.objects.get(id=id)
    return render(request, 'display-one.html', {"display": display})


def viking_era(request):
    viking = Catalogue.objects.filter(era='viking')
    newest = Catalogue.objects.filter(era='viking').last()
    context = {
        "viking": viking,
        "newest": newest
        }
    return render(request, 'viking-era.html', context)



