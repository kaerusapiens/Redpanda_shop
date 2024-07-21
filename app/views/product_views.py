from django.shortcuts import render , get_object_or_404
from app.models import Product, Category

#商品View
def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    return render(request, 'product_detail.html', {'product': product})


# possible to access in every template by 'context_processors' in template settings.py
def category_list(request):
    #categories = Category.objects.all()
    categories = Category.objects.filter(parent__isnull=True).prefetch_related('subcategories')
    return {'categories': categories}

#カテゴリーView
def category_view(request,slug):
    category = get_object_or_404(Category, slug=slug)
    subcategories = category.get_descendants(include_self=True)
    products = Product.objects.filter(category__in=subcategories)
    #products=Product.objects.filter(category=category)
    return render(request, 'category_list.html', {'category': category,'products': products})

    
def search(request):
    query = request.GET.get('q')
    results = Product.objects.filter(product_name__icontains=query) if query else []
    return render(request, 'search_results.html', {'results': results, 'query': query})