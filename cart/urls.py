from django.urls import path
from .views import CartListView, AddToCartView, remove_from_cart




"""
urlpatterns = [
    path("",views.cart_view,name="cart-view"),
    path("add/",views.cart_delete,name="cart-delete"),
    path("delete/",views.cart_add,name="cart-add"),
    path("update/",views.cart_update,name="cart-update")

]
"""
urlpatterns = [
    path("",CartListView.as_view(),name="cart-view"),
    path("add/",AddToCartView.as_view(),name="cart-add"),
    path('remove/<int:pk>/', remove_from_cart, name='cart-remove'),

]