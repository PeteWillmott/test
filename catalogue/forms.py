from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import Catalogue



class BidForm(forms.Form):
    """Passes bid to view"""
    bid = forms.DecimalField(max_digits=12, decimal_places=2)


class CatalogueForm(ModelForm):
    class Meta:
        model = Catalogue
        fields = [
            'name',
            'description',
            'era',
            'image'
        ]
