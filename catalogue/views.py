from datetime import datetime, timezone
from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Catalogue
from .forms import CatalogueForm, BidForm


def view_all(request):
    """Returns the whole catalogue to browse."""
    catalogue = Catalogue.objects.all()
    newest = Catalogue.objects.last()
    return render(request, 'display-all.html', {"catalogue": catalogue, "newest": newest})

def view_one(request, pk):
    """
    Displays details of a specific item.
    Also handles bid functions.
    """
    display = Catalogue.objects.get(id=pk)
    if not request.user.is_authenticated:
        messages.info(request, 'To view full details please login first.')
        context = {
            "display": display,
        }
        return render(request, 'display-one-closed.html', context)

    else:
        open = Catalogue.objects.filter(start__lte=datetime.now()).filter(finish__gte=datetime.now())
        finish = Catalogue.objects.filter(finish__lte=datetime.now())

        if display in finish:
            if display.last_bidder == request.user:
                return redirect('payment:billing', id=pk)
            
            context = {
                "display": display,
            }
            return render(request, 'display-one-closed.html', context)

        elif display in open:

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

        else:
            context = {
                "display": display,
            }

            return render(request, 'display-one-closed.html', context)


def view_era(request, era):
    """Returns a subset of items by historical era."""
    era_subset = Catalogue.objects.filter(era=era)
    newest = Catalogue.objects.filter(era=era).last()
    context = {
        "era_subset": era_subset,
        "newest": newest
        }
    return render(request, 'display-era.html', context)


