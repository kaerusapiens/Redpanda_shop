from typing import Any
from django.db import models
from django.utils.timezone import localtime
from django.utils import timezone
from datetime import timedelta

class Category(models.Model):
    name = models.CharField(max_length=100,db_index=True)
    slug = models.SlugField(max_length=250,unique=True)

    #Categorys→Categories
    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name
class ShippingChoices(models.TextChoices):
    # page view side / admin side
    in_stock =  'In Stock','in_stock'
    drop_ship =  'Drop Ship','drop_ship'



class Product(models.Model):
    category = models.ForeignKey(Category, related_name= 'products', on_delete=models.CASCADE,default=1)
    product_name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    product_price = models.DecimalField(max_digits=10, decimal_places=2)
    product_description = models.TextField(blank=True)
    product_image = models.ImageField(upload_to='')
    can_return = models.BooleanField(default=True)
    est_ship_date = models.CharField(max_length=10,choices=ShippingChoices.choices,default=ShippingChoices.in_stock)


    def __str__(self):
        return self.product_name

    def get_est_ship_date(self):
        if self.est_ship_date == ShippingChoices.in_stock:
            return timezone.now().date()
        elif self.est_ship_date == ShippingChoices.drop_ship:
            return timezone.now().date() + timedelta(days=7)
        return None