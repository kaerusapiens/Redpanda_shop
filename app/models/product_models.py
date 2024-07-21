from django.db import models
from django.utils import timezone
from datetime import timedelta
from django.urls import reverse
from django.utils.text import slugify


class Category(models.Model):
    id = models.AutoField(primary_key=True,editable=False)
    name = models.CharField(max_length=100,db_index=True)
    slug = models.SlugField(max_length=250,unique=True)
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='subcategories')

    def get_absolute_url(self):
        return reverse('category_list',args=[self.slug])
    #Admin panel Categorys→Categories
    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def get_descendants(self, include_self=False):
        descendants = []
        if include_self:
            descendants.append(self)
        children = self.subcategories.all()
        for child in children:
            descendants.extend(child.get_descendants(include_self=True))
        return descendants
        


class ShippingChoices(models.TextChoices):
    # page view side / admin side
    in_stock =  'In Stock','in_stock'
    drop_ship =  'Drop Ship','drop_ship'



class Product(models.Model):
    id = models.AutoField(primary_key=True,editable=False)
    category = models.ForeignKey(Category, related_name= 'products', on_delete=models.CASCADE,default=1)
    product_name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    product_price = models.DecimalField(max_digits=10, decimal_places=2)
    product_description = models.TextField(blank=True)
    product_image = models.ImageField(upload_to='')
    can_return = models.BooleanField(default=True)
    est_ship_date = models.CharField(max_length=10,choices=ShippingChoices.choices,default=ShippingChoices.in_stock)
    #reverse
    def get_absolute_url(self):
        return reverse('product_detail',args=[self.slug])

    def get_est_ship_date(self):
        if self.est_ship_date == ShippingChoices.in_stock:
            return timezone.now().date()
        elif self.est_ship_date == ShippingChoices.drop_ship:
            return timezone.now().date() + timedelta(days=7)

    def __str__(self):
        return self.product_name
    

