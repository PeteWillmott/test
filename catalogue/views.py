from django.shortcuts import render, get_object_or_404
from .models import Catalogue
from .forms import CatalogueForm

# Create your views here.

def item_create(request):
    form = CatalogueForm()
    return render(request, 'item-create.html', {"form": form})


def item_update(request, id):
    update = get_object_or_404(Catalogue, id=id)
    form = CatalogueForm(request.POST, instance=update)
    return render(request, 'item-update.html', {"form": form})
    # update code
    # return render(request, 'display-all.html', {"catalogue": catalogue, "newest": newest})


def view_all(request):
    catalogue = Catalogue.objects.all()
    newest = Catalogue.objects.last()
    return render(request, 'display-all.html', {"catalogue": catalogue, "newest": newest})


def view_one(request, id):
    display = Catalogue.objects.get(id=id)
    return render(request, 'display-one.html', {"display": display})



