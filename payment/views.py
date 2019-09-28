from django.shortcuts import render, redirect, reverse 
from .forms import Billing_Address_Form, Delivery_Address_Form, Customer_Form, Recipient_Form
from .models import Delivery_Address, Billing_Address, Customer


"""def payment(request):
    if request.method == "POST":

        billing = Billing_Address.objects.get(user=request.user)

        delivery_form = Delivery_Address_Form(request.POST, instance=request.user)
        if delivery_form.is_valid():
            delivery_form.save(commit=False)
            delivery_form.user = request.user
            delivery_form.save()
            recipient = delivery_form.cleaned_data['delivery_name']
            address = Delivery_Address.objects.get(delivery_name=recipient)
            return render(request, 'payment-details.html', {"address": address, "billing": billing})

        else:
            recipient_form = Recipient_Form(request.POST)
            if recipient_form.is_valid():
                recipient = recipient_form.cleaned_data.get('recipient')
                address = Delivery_Address.objects.get(delivery_name=recipient)
                return render(request, 'payment-details.html', {"address": address, "billing": billing})

    recipient_form = Recipient_Form(instance=request.user)
    delivery_form = Delivery_Address_Form(instance=request.user)
    context = {
        "recipient_form": recipient_form,
        "delivery_form": delivery_form
    }
    return render(request, 'delivery-address.html', context)"""


def payment(request):
    form_data = request.POST or None
    recipient_form = Recipient_Form(form_data, user=request.user)
    delivery_form = Delivery_Address_Form(form_data)
    
    if request.method == "POST":
        if delivery_form.is_valid():
            address_used = delivery_form.save(commit=False)
            address_used.user = request.user
            address_used.save()
            return render(
                request,
                "payment-details.html",
                {"address": address_used, "billing": None},
            )

        elif recipient_form.is_valid():
            address = recipient_form.cleaned_data.get("recipient")
            return render(
                request,
                "payment-details.html",
                {"address": address, "billing": None},
            )

    context = {"recipient_form": recipient_form, "delivery_form": delivery_form}
    return render(request, "delivery-address.html", context)

