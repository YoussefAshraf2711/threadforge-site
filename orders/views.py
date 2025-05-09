from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from cart.cart import Cart
from .forms import CheckoutForm
from .models import Order, OrderItem


@login_required
def checkout(request):
    """
    Show checkout form; on POST save an Order and redirect to thank-you page.
    """
    cart = Cart(request)

    # Redirect if cart is empty
    if len(cart) == 0:
        return redirect('shop:product_list')

    if request.method == "POST":
        form = CheckoutForm(request.POST)
        if form.is_valid():
            # ① create Order tied to logged-in user
            order = Order.objects.create(
                user=request.user,
                full_name=form.cleaned_data['full_name'],
                email=form.cleaned_data['email'],
                address=form.cleaned_data['address'],
            )

            # ② copy cart items ➜ OrderItem rows
            for item in cart:
                prod = item["product"]
                OrderItem.objects.create(
                    order=order,
                    product=prod.name,      # snapshot name
                    price=prod.price,
                    quantity=item["quantity"],
                )

            # ③ clear cart & thank user
            cart.clear()
            return render(
                request,
                "orders/thanks.html",
                {"name": order.full_name, "order_id": order.id},
            )
    else:
        form = CheckoutForm()

    return render(
        request,
        "orders/checkout.html",
        {"cart": cart, "form": form},
    )


@login_required
def order_history(request):
    """
    List all orders placed by the current user.
    """
    orders = request.user.orders.all().order_by("-created_at")
    return render(request, "orders/history.html", {"orders": orders})
