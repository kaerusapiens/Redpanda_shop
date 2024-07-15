from django.shortcuts import render , get_object_or_404
from .models import Product, Category


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    return render(request, 'product_detail.html', {'product': product})


# possible to access in every template by 'context_processors' in template settings.py
def category_list(request):
    categories = Category.objects.all()
    return {'categories': categories}

def category_view(request,slug):
    category = get_object_or_404(Category, slug=slug)
    products=Product.objects.filter(category=category)
    return render(request, 'category_list.html', {'category': category,'products': products})

    
