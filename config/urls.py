from django.contrib import admin
from django.urls import path, include       # ← include must be imported

urlpatterns = [
    path('admin/', admin.site.urls),

    # Cart first, so /cart/ short-circuits before hitting shop URLs
    path('cart/', include('cart.urls', namespace='cart')),

    # Shop last — catches / and /<slug>/
    path('', include('shop.urls', namespace='shop')),
]
