from .models import Products

class ProductService:
    
    ALLOWED_UPDATE_FIELDS = {"price", "description", "quantity"}
    
    @staticmethod
    def canBuy(user):
        return user.is_authenticated and user.role == 'Consumer'
    
    @staticmethod
    def canCreate(user):
        return user.is_authenticated and (user.role == 'Producer' or user.role == 'Admin')

    @staticmethod
    def canModify(user, product):
        return (
            user.is_authenticated
            and (user.role == 'Producer' or user.role == 'Admin') and
            product.producer == user
        )
    
    @staticmethod
    def listProducts(user):
        products = Products.objects.all()
        for p in products:
            p.can_edit = ProductService.canModify(user, p)
            p.can_delete = p.can_edit
            p.can_buy = ProductService.canBuy(user)
        return products

    @staticmethod
    def create(user, data):
        if not ProductService.canCreate(user):
            raise PermissionError('Not allowed')

        return Products.objects.create(
            name=data.get('name'), 
            price=data.get('price'),
            description=data.get('description'),
            category=data.get('category'),
            quantity=data.get('quantity'),
            producer = user
        )
    
    @staticmethod
    def update(user, data, product):
        if not ProductService.canModify(user, product):
            raise PermissionError('Not allowed')

        for field in ProductService.ALLOWED_UPDATE_FIELDS:
            if field in data:
                setattr(product, field, data[field])
        product.save()
        return product
    
    @staticmethod
    def delete(user, product):
        if not ProductService.canModify(user, product):
            raise PermissionError('Not allowed')
        product.delete()
        

    @staticmethod
    def getProduct(user, product):
        if not ProductService.canModify(user, product):
            raise PermissionError('Not allowed')
        product.can_edit = ProductService.canModify(user, product)
        product.can_delete = product.can_edit
        return product
        
        
        
