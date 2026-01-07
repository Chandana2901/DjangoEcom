from django.shortcuts import render, redirect
from .models import Products
from category.models import Category
from .services import ProductService
from django.contrib.auth.decorators import login_required
from api.views import GatewayProxyApi
from django.http import JsonResponse


# Create your views here.
def productList(request):
    products = Products.objects.all()
    return JsonResponse({'items': list(products.values())})  
    # products = ProductService.listProducts(request.user)
    # can_create = ProductService.canCreate(request.user)
    # return render(request, 'products/list.html', {'products': products, 'allowed': can_create})
    # gateway = GatewayProxyApi()
    # response = gateway.get(request, service='product', path='list/')
    # payload = response.json()
    
    # rights = payload.get('_ui_permissions', {})
    # return render(
    #     request,
    #     'product/list.html',
    #     {
    #         'products': payload.get('items')
    #     }
    # )

@login_required
def createProduct(request):
    if request.method == 'POST':
        categoryId = request.POST.get('category')
        category = Category.objects.get(pk=categoryId)
        ProductService.create(
            request.user,
            {
                'name':request.POST.get('name'),
                'price':request.POST.get('price'),
                'quantity': request.POST.get('quantity'),
                'description': request.POST.get('description'),
                'category': category,
            }
        )
        return redirect('products:products')
    
    categories = Category.objects.all()
    
    return render(request, 'products/createProduct.html', {'categories': categories, 'producer': request.user})


@login_required
def deleteProduct(request, product_id):
    if request.method == 'POST':
        product = Products.objects.get(pk=product_id)
        ProductService.delete(request.user, product)
        return redirect('products:products')

@login_required
def updateProduct(request, product_id):
    product = Products.objects.get(pk=product_id)
    productVal = ProductService.getProduct(request.user, product)

    if request.method == 'POST':
        data = {
            'price' : request.POST.get('price', product.price),
            'description': request.POST.get('description', product.description),
            'quantity': request.POST.get('quantity', product.quantity)
        }
        ProductService.update(user=request.user, data=data, product=product)
        return redirect('products:products')

    return render(request, 'products/updateProduct.html', {'product' : productVal})



@login_required
def buyProduct(request, product_id):
    pass