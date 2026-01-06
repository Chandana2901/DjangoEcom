from .models import Cart, CartItem


class CartService:
    
    @staticmethod
    def getOrCreateCart(user):
        return Cart.objects.get_or_create(user=user)[0]

    @staticmethod
    def addItemsToCart(user, product, quantity=1):
        cart = CartService.getOrCreateCart(user)
        item, created = CartItem.objects.get_or_create(
            cart=cart,
            product=product,
            defaults={'quantity': quantity}
        )
        if not created:
            item.quantity += quantity
        item.save()
        
        return item
    
    
    @staticmethod
    def removeItemFromCart(user, product):
        cart = CartService.getOrCreateCart(user)
        cartItem  = CartItem.objects.filter(cart=cart, product=product)
        cartItem.delete()
        
    @staticmethod
    def getCart(user):
        return Cart.objects.prefetch_related('items__product').get(user=user)
    
    @staticmethod
    def getCartItems(user):
        cart = CartService.getCart(user)
        return cart.items.all()
    
    @staticmethod
    def getCartTotal(user):
        cart = CartService.getCart(user)
        total = 0
        for item in cart.items.all():
            total += item.product.price * item.quantity
        return total
    
    