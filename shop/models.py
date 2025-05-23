from django.db import models

# Create your models here.
from django.db import models

class Product(models.Model):
    name        = models.CharField(max_length=120)
    slug        = models.SlugField(unique=True)
    description = models.TextField(blank=True)
    price       = models.DecimalField(max_digits=8, decimal_places=2)
    image       = models.ImageField(upload_to="products/", blank=True)

    def __str__(self):
        return self.name
