from django import forms
from .models import Catalogue

class CatalogueForm(forms.ModelForm):
    class Meta:
        model = Catalogue
        fields = [
            'name',
            'description',
            'price',
            'culture',
            'era',
            'image'
        ]


class BidForm(forms.ModelForm):
    bid = forms.DecimalField(max_digits=12, decimal_places=2)
    class Meta:
        model = Catalogue
        fields = ['bid']

    def clean_bid(self):
        bid = self.cleaned_data.get('bid')
        return bid