from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Billing_Address(models.Model):
    PROF = 'Prof'
    DR = 'Dr'
    LADY = 'Lady'
    MRS = 'Mrs'
    MS = 'Ms'
    MISS = 'Miss'
    MR = 'Mr'
    SIR = 'Sir'
    TITLE_CHOICES = [
        (PROF, 'Prof'),
        (DR, 'Dr'),
        (LADY, 'Lady'),
        (MRS, 'Mrs'),
        (MS, 'Ms'),
        (MISS, 'Miss'),
        (MR, 'Mr'),
        (SIR, 'Sir'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=4, choices=TITLE_CHOICES, default=MRS)
    billing_name = models.CharField(max_length=80)
    street1 = models.CharField(max_length=100)
    street2 = models.CharField(max_length=100, blank=True)
    town = models.CharField(max_length=50)
    county = models.CharField(max_length=50)
    postcode = models.CharField(max_length=20)
    country = models.CharField(max_length=50)

    def __str__(self):
        return self.billing_name


class Delivery_Address(models.Model):
    PROF = 'Prof'
    DR = 'Dr'
    LADY = 'Lady'
    MRS = 'Mrs'
    MS = 'Ms'
    MISS = 'Miss'
    MR = 'Mr'
    SIR = 'Sir'
    TITLE_CHOICES = [
        (PROF, 'Prof'),
        (DR, 'Dr'),
        (LADY, 'Lady'),
        (MRS, 'Mrs'),
        (MS, 'Ms'),
        (MISS, 'Miss'),
        (MR, 'Mr'),
        (SIR, 'Sir'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=4, choices=TITLE_CHOICES, default=MRS)
    delivery_name = models.CharField(max_length=100)
    street1 = models.CharField(max_length=100)
    street2 = models.CharField(max_length=100, blank=True)
    town = models.CharField(max_length=50)
    county = models.CharField(max_length=50)
    postcode = models.CharField(max_length=20)
    country = models.CharField(max_length=50)

    def __str__(self):
        return self.delivery_name





