from django.shortcuts import redirect, render, get_object_or_404
from shop.models import Product
from .cart import Cart
from .forms import CartAddForm             # ← make sure this import is present

def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)

    form = CartAddForm(request.POST)
    print("POST-DATA:", request.POST)          # ① debug
    print("FORM-ERRORS:", form.errors)         # ② debug

    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product,
                 quantity=cd['quantity'],
                 update=cd['update'])
    return redirect('cart:cart_detail')


def cart_update(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product, quantity=cd['quantity'], update=True)
    return redirect('cart:cart_detail')

def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')

def cart_detail(request):
    cart = Cart(request)
    return render(request, 'cart/detail.html', {'cart': cart})
