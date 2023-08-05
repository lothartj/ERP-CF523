from django.db import models

# Create your models here.
class Items(models.Model):
    itemcode = models.CharField(max_length=10)
    description = models.CharField(max_length=50)
    barcode = models.CharField(max_length=20)
    unitmeasure = models.CharField(max_length=5)
    inventory = models.IntegerField()
    unitcost = models.DecimalField(max_digits=10000000000, decimal_places=2)
    image = models.ImageField(upload_to='img/%Y', null=True, blank=True)

class Login(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=50)

