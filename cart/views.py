from django.shortcuts import render

def cart_view(request):
    return render(request, 'cart.html')


def cart_add(request):
    return render(request, 'cart.html')


def cart_delete(request):
    return render(request, 'cart.html')


def cart_update(request):
    return render(request, 'cart.html')