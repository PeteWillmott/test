from django.shortcuts import render, get_object_or_404
from .models import Catalogue
from .forms import CatalogueForm

# Create your views here.

# @login_required
# require admin login
def item_create(request):
    if request.method == "POST":
        form = CatalogueForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            form = CatalogueForm()

    else:
        form = CatalogueForm()
    return render(request, 'item-create.html', {"form": form})


# @login_required
# require admin login
def item_update(request, id):
    #if request.method == "POST":

    update = get_object_or_404(Catalogue, id=id)
    form = CatalogueForm(request.POST, instance=update)
    return render(request, 'item-update.html', {"form": form})
    # update code
    # newset = ...
    # return render(request, 'display-all.html', {"catalogue": catalogue, "newest": newest})


def view_all(request):
    catalogue = Catalogue.objects.all()
    newest = Catalogue.objects.last()
    return render(request, 'display-all.html', {"catalogue": catalogue, "newest": newest})


def view_one(request, id):
    display = Catalogue.objects.get(id=id)
    return render(request, 'display-one.html', {"display": display})



