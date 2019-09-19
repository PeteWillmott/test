from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from catalogue.models import Catalogue

# Create your models here.
class News(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField(null=True)
    image = models.ImageField(upload_to='images/', blank=True)
    pub_date = models.DateTimeField(default=timezone.now,)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "News"

    def __str__(self):
        return self.title


class Review(models.Model):
    title = models.CharField(max_length=200)
    productID = models.ForeignKey(Catalogue, on_delete=models.CASCADE)
    text = models.TextField(null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(default=timezone.now,)

    def __str__(self):
        return self.title