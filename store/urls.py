from django.urls import path
from .views import product_detail, category_list


urlpatterns = [
    path('p/<slug:slug>',  product_detail, name='product_detail'),
    path('c/<slug:slug>',  category_list, name='category_list'),
]
