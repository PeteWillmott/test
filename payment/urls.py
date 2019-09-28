from django.urls import path, include
from . import views
from .models import Customer, Billing_Address, Delivery_Address
from .forms import Customer_Form, Billing_Address_Form, Delivery_Address_Form

app_name = 'payment'
urlpatterns = [
    #path('customer', views.customer_details, name="customer-details"),
    #path('shipping', views.shipping_details, name="shipping-details"),
    path('', views.payment, name="payment-details"),
    #path('pay', views.payment_details, name="payment-details"),
]