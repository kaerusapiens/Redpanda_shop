from django.urls import path
from .views import CartListView, AddToCartView, remove_from_cart



urlpatterns = [
    path("",CartListView.as_view(),name="cart-view"),
    path("add/",AddToCartView.as_view(),name="cart-add"),
    path('remove/<int:pk>/', remove_from_cart, name='cart-remove'),

]