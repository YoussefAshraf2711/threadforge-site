from django.db import models
from django.contrib.auth.models import User


class Order(models.Model):
    user        = models.ForeignKey(
        User, related_name="orders",
        on_delete=models.SET_NULL, null=True, blank=True
    )
    full_name   = models.CharField(max_length=60)
    email       = models.EmailField()
    address     = models.TextField()
    created_at  = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order #{self.id} – {self.full_name}"

    @property
    def total_price(self):
        return sum(item.subtotal for item in self.items.all())


class OrderItem(models.Model):
    order    = models.ForeignKey(Order, related_name="items", on_delete=models.CASCADE)
    product  = models.CharField(max_length=120)          # snapshot of name
    price    = models.DecimalField(max_digits=8, decimal_places=2)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.product} ×{self.quantity}"

    @property
    def subtotal(self):
        return self.price * self.quantity
