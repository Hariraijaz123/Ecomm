from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='products/')
    price = models.DecimalField(max_digits=20,decimal_places=2)
    active = models.BooleanField(default=True)

    def __unicode__(self):
        return self.title

class Variation(models.Model):
    product = models.ForeignKey(Product)
    title = models.CharField(max_length=100, null=True, blank=True)
    price = models.DecimalField(max_digits=20,decimal_places=2)
    sale_price = models.DecimalField(max_digits=20,decimal_places=2)
    active = models.BooleanField(default=True)
    inventory = models.IntegerField()

    def __unicode__(self):
        return self.title

class Category(models.Model):
    product = models.ForeignKey(Product)
    title = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    active = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __unicode__(self):
        return self.title

class Featured_Product(models.Model):
    product = models.ForeignKey(Product)
    title = models.CharField(max_length=100, null=True, blank=True)
    image = models.ImageField(upload_to='products/')
    text = models.TextField(null=True, blank=True)
    show_price = models.DecimalField(max_digits=20,decimal_places=2)
    active = models.BooleanField(default=True)

    def __unicode__(self):
        return self.title
