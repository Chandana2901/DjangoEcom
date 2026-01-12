from rest_framework import serializers
from .models import CartItem

class CartItemSeralizer(serializers.ModelSerializer):
    cart = serializers.CharField(source='cart.user', read_only=True)
    product = serializers.CharField(source='product.name', read_only=True)
    productPrice = serializers.FloatField(source='product.price', read_only=True)
    subtotal = serializers.SerializerMethodField()
    
    class Meta:
        model = CartItem
        fields = ['id', 'cart', 'product', 'productPrice', 'quantity', 'subtotal']
    
    def get_subtotal(self, obj):
        return str(obj.product.price * obj.quantity)