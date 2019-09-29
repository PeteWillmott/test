from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import Billing_Address, Delivery_Address


class Billing_Address_Form(ModelForm):
    class Meta:
        model = Billing_Address
        fields = [
            'title',
            'billing_name',
            'street1',
            'street2',
            'town',
            'county',
            'postcode',
            'country'
        ]


class Delivery_Address_Form(ModelForm):
    class Meta:
        model = Delivery_Address
        labels = {'delivery_name': 'Recipient\'s name'}
        fields = [
            'title',
            'delivery_name',
            'street1',
            'street2',
            'town',
            'county',
            'postcode',
            'country'
        ]


class RecipientModelChoiceField(forms.ModelChoiceField):
    """Pick a recipient from multiple delivery addresses"""
    def label_from_instance(self, address):
        return f"{address.delivery_name}, {address.street1}"


class Recipient_Form(forms.Form):
    recipient = RecipientModelChoiceField(
        queryset=None,
        widget=forms.RadioSelect,
        empty_label=None
    )

    def __init__(self, *args, user=None, **kwargs):
        if user is None:
            raise ValueError("Missing user")
        super().__init__(*args, **kwargs)
        self.fields['recipient'].queryset = Delivery_Address.objects.filter(user=user)

    def clean_recipient(self):
        recipient = self.cleaned_data.get('recipient')
        return recipient