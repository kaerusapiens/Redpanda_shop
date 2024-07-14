from django.shortcuts import render , get_object_or_404
from .models import Product, Category



def product_list(request):
    products = Product.objects.all()
    for product in products:
        product.estimated_shipping_date = product.get_est_ship_date()
    return render(request, 'product_list.html', {'products': products})



def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'product_detail.html', {'product': product})

