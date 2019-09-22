from django import forms
from django.contrib.auth.models import User
from .models import Billing_Address, Delivery_Address


class Billing_AddressForm(forms.ModelForm):
    class Meta:
        model = Billing_Address
        fields =[
            'billing_name',
            'street1',
            'street2',
            'town',
            'county',
            'postcode',
            'country'
        ]


class Delivery_AddressForm(forms.ModelForm):
    class Meta:
        model = Delivery_Address
        fields =[
            'delivery_name',
            'street1',
            'street2',
            'town',
            'county',
            'postcode',
            'country'
        ]