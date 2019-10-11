from django.urls import path, include
from .views import billing, payment
from .models import Billing_Address, Delivery_Address
from .forms import Billing_Address_Form, Delivery_Address_Form

app_name = 'payment'
urlpatterns = [
    path('pay<pk>', payment, name="payment"),
    path('<pk>', billing, name="billing"),
]