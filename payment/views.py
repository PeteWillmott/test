from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from .forms import Billing_Address_Form, Delivery_Address_Form,  Recipient_Form
from .models import Delivery_Address, Billing_Address
from catalogue.models import Catalogue

@login_required(login_url='/login/')
def billing(request, id):
    """Displays registered billing address for confirmation or blank form for a new address."""
    form_data = request.POST or None
    try:
        instance =  Billing_Address.objects.get(user=request.user)
    except ObjectDoesNotExist:
        instance = None
    billing_form = Billing_Address_Form(form_data, instance=instance)

    if request.method == "POST":
        if billing_form.is_valid():
            billing_address = billing_form.save(commit=False)
            billing_address.user = request.user
            billing_address.save()
            return redirect('payment:payment', id=id)

    return render(request, "billing-address.html", {"billing_form": billing_form})


@login_required(login_url='/login/')
def payment(request, id):

    """Allows selection or entry of delivery address, displays addresses, item details and stripe payment form."""
    form_data = request.POST or None
    recipient_form = Recipient_Form(form_data, user=request.user)
    delivery_form = Delivery_Address_Form(form_data)
    billing = Billing_Address.objects.get(user=request.user)
    item = Catalogue.objects.get(id=id)
    
    if request.method == "POST":
        if delivery_form.is_valid():
            address_used = delivery_form.save(commit=False)
            address_used.user = request.user
            address_used.save()
            return render(
                request,
                "payment-details.html",
                {"address": address_used,
                "billing": billing,
                "item": item},
            )

        elif recipient_form.is_valid():
            address = recipient_form.cleaned_data.get("recipient")
            return render(
                request,
                "payment-details.html",
                {"address": address,
                "billing": billing,
                "item": item},
            )

    recipient_check = Delivery_Address.objects.filter(user=request.user)
    if recipient_check:
        context = {"recipient_form": recipient_form, "delivery_form": delivery_form}
    else:
        context = {"delivery_form": delivery_form}
    return render(request, "delivery-address.html", context)


@login_required(login_url='/login/')
def stripe(request, id):
    item = Catalogue.objects.get(id=id)
    if request.method == 'POST':
        token = request.POST.get['stripeToken']
        try:
            charge = stripe.Charge.create(
                amount=item.bid,
                currency='gbp',
                description=item.name,
                source=token,
            )

        except:
            messages.error(request, f"Your card was declined!")

    if charge.paid:
        return render(request, "success.html")

    return redirect('payment:payment', id=id)