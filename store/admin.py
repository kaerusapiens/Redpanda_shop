from django.contrib import admin
from .models import Product, Category


#creating prepoulated field
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'product_price','product_description', 'can_return','est_ship_date')
    prepopulated_fields = {'slug': ('product_name',)}