from django.db import models
from django.contrib.auth.models import User


class Customer(models.Model):
    MR = 'MR'
    MRS = 'MRS'
    MS = 'MS'
    DR = 'DR'
    PROF = 'PROF'
    TITLE_CHOICES = [
    ('MR', 'Mr'),
    ('MRS', 'Mrs'),
    ('MS', 'Ms'),
    ('DR','Dr'),
    ('PROF','Prof'),
    ]
    customerID = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=4, choices=TITLE_CHOICES, default=MRS)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)

    def __str__(self):
        return self.last_name


class Billing_Address(models.Model):
    customerID = models.ForeignKey(User, on_delete=models.CASCADE)
    billing_name = models.CharField(max_length=200)
    street1 = models.CharField(max_length=200)
    street2 = models.CharField(max_length=200)
    town = models.CharField(max_length=200)
    county = models.CharField(max_length=200)
    postcode = models.CharField(max_length=20)
    country = models.CharField(max_length=200)

    def __str__(self):
        return self.billing_name


class Delivery_Address(models.Model):
    customerID = models.ForeignKey(User, on_delete=models.CASCADE)
    delivery_name = models.CharField(max_length=200)
    street1 = models.CharField(max_length=200)
    street2 = models.CharField(max_length=200)
    town = models.CharField(max_length=200)
    county = models.CharField(max_length=200)
    postcode = models.CharField(max_length=20)
    country = models.CharField(max_length=200)

    def __str__(self):
        return self.delivery_name





