from django.contrib import admin
from django.urls import path, include       # ← include must be imported
from django.contrib.auth import views as auth_views
from accounts import views as acc_views       # type: ignore # we’ll create this in a moment

urlpatterns = [
    path('admin/', admin.site.urls),

    path('cart/',      include('cart.urls',    namespace='cart')),
    path('checkout/',  include('orders.urls',  namespace='orders')),

    # --- auth ---
    path('accounts/login/',  auth_views.LoginView.as_view(
            template_name='accounts/login.html'), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(
            next_page='shop:product_list'),       name='logout'),
    path('accounts/signup/', acc_views.signup,    name='signup'),

    path('',            include('shop.urls',   namespace='shop')),
]
