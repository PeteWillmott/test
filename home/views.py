from django.shortcuts import render
from catalogue.models import Catalogue

def index(request):
    """Return the index.html file."""
    newest_picture = Catalogue.objects.last()
    return render(request, 'index.html', {"newest_picture": newest_picture})
