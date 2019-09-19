from django.shortcuts import render
from .forms import CustomerForm, Billing_AddressForm, Delivery_AddressForm

def customer_details(request):
    form = CustomerForm
    return render(request, 'customer-details.html', {"form": form})

def shipping_details(request):
    form = Delivery_AddressForm
    return render(request, 'shipping-details.html', {"form": form})

def billing_details(request):
    form = Billing_AddressForm
    return render(request, 'billing-details.html', {"form": form})


def payment_details(request):
    return render(request, 'payment-details.html')
