
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import index





urlpatterns = [
    #Index url
    path('', index, name='index'),
    #admin url
    path('admin/', admin.site.urls),
    #store app
    path('', include('store.urls')),
    #cart app
    path('cart/', include('cart.urls')),
    #account app
    path('', include('account.urls')),
    #debug toolbar
    path('__debug__/', include('debug_toolbar.urls')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
