from django.shortcuts import render
from .forms import Billing_AddressForm, Delivery_AddressForm
from accounts.forms import CustomerForm

def customer_details(request):
    if request.method == "POST":
        form = CustomerForm(request.POST, instance=request.user)
        if form.is_valid():
            customer = form.cleaned_data['customer']
    else:
        form = CustomerForm(instance=request.user)

    return render(request, 'customer-details.html', {"form": form})

def shipping_details(request):
    form = Delivery_AddressForm(instance=request.user)
    return render(request, 'shipping-details.html', {"form": form})

def billing_details(request):
    billing_form = Billing_AddressForm(instance=request.user)
    delivery_form = Delivery_AddressForm(instance=request.user)
    return render(request, 'billing-details.html', {"billing_form": billing_form, "delivery_form": delivery_form})


def payment_details(request):
    return render(request, 'payment-details.html')
