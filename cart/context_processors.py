from .cart import Cart

def cart_item_count(request):
    """
    Add `cart_item_count` to every template context.
    Returns 0 if the cart is empty or has not been created yet.
    """
    cart = Cart(request)
    return {"cart_item_count": len(cart)}
