from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
import datetime


class Catalogue(models.Model):
    name = models.CharField(max_length=254, default='')
    sale_status = models.BooleanField(default=False)
    description = models.TextField()
    era = models.CharField(max_length=254, default='')
    image = models.ImageField(upload_to='images')
    start = models.DateTimeField("Auction starts", null=True)
    finish = models.DateTimeField("Auction finishes", null=True)
    reserve = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    increment = models.DecimalField(max_digits=10, decimal_places=2, default=10)
    bid = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    last_bidder = models.ForeignKey(User, on_delete=models.CASCADE, default='', null=True, blank=True)


    def __str__(self):
        return self.name


    def get_absolute_url(self):
        return reverse("catalogue:view_one", args=[str(self.pk)])



