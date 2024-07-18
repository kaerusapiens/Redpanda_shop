from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView



urlpatterns = [
    path('logout/', LogoutView.as_view(), name='logout'), #HTMLなしでpath通すことで動けるように
    path('login/', views.Login.as_view(), name='login'),
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('account/', views.AccountUpdateView.as_view(), name='account'),
]
