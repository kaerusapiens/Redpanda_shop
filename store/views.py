from django.shortcuts import render , get_object_or_404
from .models import Product, Category



def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    return render(request, 'product_detail.html', {'product': product})

def category_list(request,slug):
    categories = Category.objects.all(slug=slug)
    return render(request, 'header.html', {'categories': categories})

    
