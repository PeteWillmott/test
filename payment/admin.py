from django.contrib import admin
from .models import Customer, Billing_Address, Delivery_Address

admin.site.register(Customer)
admin.site.register(Billing_Address)
admin.site.register(Delivery_Address)
