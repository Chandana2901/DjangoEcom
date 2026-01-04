from django.shortcuts import render, redirect
from .models import Products
from .utils import checkPermission
from category.models import Category
from users.models import Users

# Create your views here.
def productList(request):
    products = Products.objects.all()
    isProducer = request.user.is_authenticated and request.user.role == 'Producer'
    return render(request, 'products/list.html', {'products': products, 'allowed': isProducer})

def createProduct(request):
    if request.method == 'POST':
        checkPermission(request)
        name = request.POST.get('name')
        price = request.POST.get('price')
        quantity = request.POST.get('quantity')
        categoryId = request.POST.get('category')
        category = Category.objects.get(pk=categoryId)
        producerUser = request.POST.get('producer', request.user)
        producer = Users.objects.get(name=producerUser)
        description = request.POST.get('description')

        Products.objects.create(
            name=name,
            price=price,
            quantity=quantity,
            category=category,
            producer=producer,
            description=description
        )
        return redirect('products:products')
    
    categories = Category.objects.all()
    
    return render(request, 'products/createProduct.html', {'categories': categories, 'producer': request.user})


def deleteProduct(request, product_id):
    if request.method == 'POST':
        checkPermission(request)
        product = Products.objects.filter(pk=product_id)
        product.delete()
        return redirect('products:products')
    