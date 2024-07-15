from store.models import Product
from django.shortcuts import render 

def index(request):
    products = Product.objects.all()
    return render(request, 'index.html', {'products': products})