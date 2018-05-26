from django.db import models

# Create your models here.

class Buyer(models.Model):
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.CharField(max_length=250)

class Seller(models.Model):
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.CharField(max_length=250)
    miles = models.IntegerField()
    price = models.FloatField(null=True, blank=True, default=None)
