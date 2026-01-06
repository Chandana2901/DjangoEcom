from django.shortcuts import render, redirect
from .services import CartService
from products.models import Products
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def viewCart(request):
    cart = CartService.getOrCreateCart(request.user)
    items = cart.items.all()
    total = CartService.getCartTotal(request.user)
    data = {
        'cart': cart,
        'items': items,
        'total': total
    }
    return render(request, 'cart/view.html', data)
    

@login_required
def addToCart(request, product_id):
    if request.method == 'POST':
        product = Products.objects.get(pk=product_id)
        CartService.addItemsToCart(request.user, product)
        return redirect('cart:viewCart')

    return redirect('products:products')