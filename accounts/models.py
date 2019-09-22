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
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=4, choices=TITLE_CHOICES, default=MRS)

    def __str__(self):
        return self.user.username