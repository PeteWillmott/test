from django import forms
from django.forms import ModelForm
from .models import Bid

class BidForm(ModelForm):
    class Meta:
        model = Bid
        fields = ('bid', 'user', 'product')