from django.db import models


# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=70, blank=False, default='')
    age = models.IntegerField(blank=False, default=1)
    address = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
