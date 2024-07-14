from django.urls import path
from . import views
from .views import store, product_detail


urlpatterns = [
    path('', store, name='store'),
    path('<slug:slug>',  product_detail, name='product_detail'),
    # Add more URL patterns as needed
]
