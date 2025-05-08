from django.shortcuts import render, redirect
from cart.cart import Cart
from .forms import CheckoutForm

def checkout(request):
    cart = Cart(request)
    if len(cart) == 0:
        return redirect('shop:product_list')

    if request.method == "POST":
        form = CheckoutForm(request.POST)
        if form.is_valid():
            # --- here you could save an Order model ---
            # For now we just clear the cart and thank the user.
            cart.clear()
            return render(request, 'orders/thanks.html',
                          {'name': form.cleaned_data['full_name']})
    else:
        form = CheckoutForm()

    return render(request, 'orders/checkout.html',
                  {'cart': cart, 'form': form})
