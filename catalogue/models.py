from django.db import models
from django.urls import reverse


class Catalogue(models.Model):
    name = models.CharField(max_length=254, default='')
    sale_status = models.BooleanField(default=False)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2, default='')
    culture = models.CharField(max_length=254, default='')
    era = models.CharField(max_length=254, default='')
    image = models.ImageField(upload_to='images')
    start = models.DateTimeField("Auction starts", null=True)
    finish = models.DateTimeField("Auction finishes", null=True)
    reserve = models.DecimalField(max_digits=10, decimal_places=2)
    increment = models.DecimalField(max_digits=10, decimal_places=2)
    


    def __str__(self):
        return self.name


    def get_absolute_url(self):
        return reverse("catalogue:view_one", args=[str(self.pk)])


