from django.contrib import admin
from django.urls import path, include
from app import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView

urlpatterns = [
    #Index
    path('', views.index,name= "index"),
    # User
    path('admin/', admin.site.urls),
    path('logout/', LogoutView.as_view(), name='logout'), #HTMLなしでpath通すことで動けるように
    path('login/', views.Login.as_view(), name='login'),
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('account/', views.AccountUpdateView.as_view(), name='account'),

    #Password management
    path('reset_password/', PasswordResetView.as_view(), name='reset_password'),
    path('reset_password_sent/', PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset_password_complete/', PasswordResetCompleteView.as_view(), name='password_reset_complete'),


    # Cart
    path("cart/",views.CartListView.as_view(),name="cart-view"),
    path("cart/add/",views.AddToCartView.as_view(),name="cart-add"),
    path('cart/remove/<int:pk>/', views.remove_from_cart, name='cart-remove'),
    path('cart/update/<int:pk>/', views.UpdateCartView.as_view(), name='cart-update'),
    
    #order
    path('checkout/', views.CheckoutView.as_view(), name = 'checkout'),
    path('order-confirmation/', views.OrderConfirmationView.as_view(), name='order_confirmation'),

    # Product
    path('p/<slug:slug>',  views.product_detail, name='product_detail'),
    path('c/<slug:slug>',  views.category_view, name='category_list'),
    path('search/', views.search, name='search'),


     #debug toolbar
    path('__debug__/', include('debug_toolbar.urls')),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
