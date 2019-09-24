from django.contrib import admin
from .models import Billing_Address, Customer, Delivery_Address

admin.site.register(Billing_Address)
admin.site.register(Customer)
admin.site.register(Delivery_Address)
