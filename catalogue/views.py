from django.shortcuts import render, get_object_or_404
from .models import Catalogue
from bid.models import Bid
from .forms import CatalogueForm
from bid.forms import BidForm

def view_all(request):
    catalogue = Catalogue.objects.all()
    newest = Catalogue.objects.last()
    return render(request, 'display-all.html', {"catalogue": catalogue, "newest": newest})


def view_one(request, pk):
    display = Catalogue.objects.get(id=pk)

    if request.method == 'POST':
        form = BidForm(request.POST)
        if form.is_valid():
            form.save()
    
    else:
        form = BidForm()

    context = {
        "display": display,
        "form": form
    }
    return render(request, 'display-one.html', context)


def viking_era(request):
    viking = Catalogue.objects.filter(era='viking')
    newest = Catalogue.objects.filter(era='viking').last()
    context = {
        "viking": viking,
        "newest": newest
        }
    return render(request, 'viking-era.html', context)



