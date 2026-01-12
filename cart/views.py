from django.shortcuts import render, redirect
from .services import CartService
from products.models import Products
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import JsonResponse
from .models import Cart, CartItem
from .serializers import CartItemSeralizer


# Create your views here.
@csrf_exempt
def viewCart(request):
    user = request.headers.get('X-User-Id')
    cart = Cart.objects.prefetch_related('items__product').get(user=user)
    items = cart.items.all()
    total = 0
    for item in items:
        total += item.product.price * item.quantity
    serializers = CartItemSeralizer(items, many=True)
    data = {
        'cart': cart.id,
        'items': serializers.data,
        'total': total
    }
    return JsonResponse({'data': data}, status=200)
    

@csrf_exempt
def addToCart(request, product_id):
    if request.method == 'POST':
        product = Products.objects.get(pk=product_id)
        user = request.headers.get('X-User-Id')
        cart = Cart.objects.get_or_create(user=user)[0]
        data = json.loads(request.body)
        item, created = CartItem.objects.get_or_create(
            cart=cart,
            product=product,
            defaults={'quantity': int(data.get('quantity', 1))}
        )
        if not created:
            item.quantity += int(data.get('quantity', 1))
        item.save()
        return JsonResponse({'message': 'Item added to cart successfully'}, status=200)