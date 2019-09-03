from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class News(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField
    image = models.ImageField(upload_to='images/')
    pub_date = models.DateTimeField(default=timezone.now,)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Review(models.Model):
    title = models.CharField(max_length=200)
    productID = models.ForeignKey(Catalogue.id, on_delete=models.CASCADE)
    text = models.TextField
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(default=timezone.now,)

    def __str__(self):
        return self.title