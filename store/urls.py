from django.urls import path
from .views import product_detail, category_view


urlpatterns = [
    path('p/<slug:slug>',  product_detail, name='product_detail'),
    path('c/<slug:slug>',  category_view, name='category_list'),
]
