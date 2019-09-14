from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from catalogue.models import Catalogue

class = Bid(models.Model):
    product = models.ForeignKey(Catalogue, on_delete=models.CASCADE)
    top_bidding = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="current highest bidding user")
    current_bid = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
            return self.product

