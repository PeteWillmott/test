from django.shortcuts import render
from .forms import Billing_AddressForm, Delivery_AddressForm, Customer_Form, Recipient_Form
from .models import Delivery_Address

"""def customer_details(request):
    if request.method == "POST":
        form = Customer_Form(request.POST, instance=request.user)
        if form.is_valid():
            customer = form.cleaned_data['customer']
    else:
        form = Customer_Form(instance=request.user)

    return render(request, 'customer-details.html', {"form": form})"""

"""def shipping_details(request):
    customer_form = Customer_Form(instance=request.user)
    delivery_form = Delivery_AddressForm(instance=request.user)
    return render(request, 'shipping-details.html', {"customer_form": customer_form, "delivery_form": delivery_form})"""

def billing_details(request):
    if request.method == "POST":
        recipient_form = Recipient_Form(request.POST)
        if recipient_form.is_valid():
            recipient = recipient_form.cleaned_data.get('recipient')
            address = Delivery_Address.objects.get(delivery_name=recipient)

        return render(request, 'payment-details.html', {"address": address})

    recipient_form = Recipient_Form(instance=request.user)
    customer_form = Customer_Form(instance=request.user)
    billing_form = Delivery_AddressForm(instance=request.user)
    delivery_form = Delivery_AddressForm(instance=request.user)
    context = {
        "recipient_form": recipient_form,
        "customer_form": customer_form,
        "billing_form": billing_form,
        "delivery_form": delivery_form
    }
    return render(request, 'billing-details.html', context)


def payment_details(request):
    return render(request, 'payment-details.html')
