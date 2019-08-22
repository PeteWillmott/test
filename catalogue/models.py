from django.db import models


class Catalogue(models.Model):
    name = models.CharField(max_length=254, default='')
    sale_status = models.BooleanField(default=False)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.name


