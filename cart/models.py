from django.db import models
from users.models import Users
from products.models import Products

# Create your models here.
class Cart(models.Model):
    user = models.OneToOneField(Users, on_delete=models.CASCADE)
    

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    class Meta:
        unique_together = ('cart', 'product')