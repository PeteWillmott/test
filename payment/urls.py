from django.urls import path, include
from . import views
from .models import Customer, Billing_Address, Delivery_Address
from .forms import CustomerForm, Billing_AddressForm, Delivery_AddressForm

app_name = 'payment'
urlpatterns = [
    path('customer', views.customer_details, name="customer-details"),
    path('shipping', views.shipping_details, name="shipping-details"),
    path('billing', views.billing_details, name="billing-details"),
    path('payment', views.payment_details, name="payment-details"),
]