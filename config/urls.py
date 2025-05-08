from django.contrib import admin
from django.urls import path, include       # ← include must be imported

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cart/',   include('cart.urls',   namespace='cart')),
    path('checkout/', include('orders.urls', namespace='orders')),
    path('',        include('shop.urls',   namespace='shop')),
]
