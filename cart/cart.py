from decimal import Decimal
from django.conf import settings
from shop.models import Product

class Cart:
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get('cart')
        if cart is None:
            cart = self.session['cart'] = {}
        self.cart = cart

    def add(self, product, quantity=1, update=False):
        prod_id = str(product.id)
        if prod_id not in self.cart:
            self.cart[prod_id] = {'quantity': 0, 'price': str(product.price)}
        if update:
            self.cart[prod_id]['quantity'] = quantity
        else:
            self.cart[prod_id]['quantity'] += quantity
        self.save()

    def remove(self, product):
        prod_id = str(product.id)
        if prod_id in self.cart:
            del self.cart[prod_id]
            self.save()

    def save(self):
        self.session.modified = True

    def __iter__(self):
        prod_ids = self.cart.keys()
        products = Product.objects.filter(id__in=prod_ids)
        for product in products:
            item = self.cart[str(product.id)]
            item['product'] = product
            item['total'] = Decimal(item['price']) * item['quantity']
            yield item

    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())

    def get_total_price(self):
        return sum(Decimal(item['price']) * item['quantity']
                   for item in self.cart.values())

    def clear(self):
        self.session['cart'] = {}
        self.save()
