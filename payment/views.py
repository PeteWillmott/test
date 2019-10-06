from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from .forms import Billing_Address_Form, Delivery_Address_Form,  Recipient_Form
from .models import Delivery_Address, Billing_Address
from catalogue.models import Catalogue

@login_required(login_url='/login/')
def payment(request):

    form_data = request.POST or None
    recipient_form = Recipient_Form(form_data, user=request.user)
    delivery_form = Delivery_Address_Form(form_data)
    billing = Billing_Address.objects.get(user=request.user)
    item = Catalogue.object.get(last_bidder=request.user)
    
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


<<<<<<< HEAD
@login_required(login_url='/login/')
=======
@login_required
>>>>>>> 8082be870b411c8693aaebbe37006a778c962dd8
def billing(request):
    form_data = request.POST or None
    instance =  Billing_Address.objects.get(user=request.user)
    billing_form = Billing_Address_Form(form_data, instance=instance)

    if request.method == "POST":
        if billing_form.is_valid():
            billing_form.save()
            return redirect(reverse('payment:payment'))

    return render(request, "billing-address.html", {"billing_form": billing_form})

