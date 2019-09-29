from django.shortcuts import render, get_object_or_404
from .models import Catalogue
from .forms import CatalogueForm, BidForm


def view_all(request):
    catalogue = Catalogue.objects.all()
    newest = Catalogue.objects.last()
    return render(request, 'display-all.html', {"catalogue": catalogue, "newest": newest})


def view_one(request, pk):
    display = Catalogue.objects.get(id=pk)

    if request.method == 'POST':
        form = BidForm(request.POST)
        if form.is_valid():
            display.bid = form.cleaned_data.get('bid')
            display.last_bidder = request.user
            display.save()

    else:
        bid_val = display.bid
        form = BidForm(initial={'bid': bid_val})

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



