from django.shortcuts import render, redirect
from .models import Products
from category.models import Category
from .services import ProductService
from django.contrib.auth.decorators import login_required
from api.views import GatewayProxyApi
from django.http import JsonResponse
from .serializers import ProductSerializer
from django.views.decorators.csrf import csrf_exempt
import json
from users.models import Users

# Create your views here.
def productList(request):
    products = Products.objects.select_related('category', 'producer')
    serializer = ProductSerializer(products, many=True)
    return JsonResponse({'items': serializer.data})  
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

@csrf_exempt
def createProduct(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        # category = Category.objects.get(pk=categoryId)
        producerId = request.headers.get('X-User-Id')
        producer = Users.objects.get(pk=producerId)
        category = Category.objects.get(pk=data.get('category'))
        product = Products.objects.create(
            # request.user,
            # {
                name=data.get('name'),
                price=data.get('price'),
                quantity=data.get('quantity'),
                description=data.get('description'),
                category=category,
                producer=producer
            # }
        )
        # return redirect('products:products')
        return JsonResponse({'message': 'Product created successfully', 'product_id': product.id}, status=201)
    
    # categories = Category.objects.all()
    
    # return render(request, 'products/createProduct.html', {'categories': categories, 'producer': request.user})
    return JsonResponse({'error': 'Invalid request method'}, status=400)


@csrf_exempt
def deleteProduct(request, product_id):
    if request.method == 'POST':
        product = Products.objects.get(pk=product_id)
        product.delete()
        return redirect('products:products')

@csrf_exempt
def getProduct(request, product_id):
    product = Products.objects.get(pk=product_id)
    productData = ProductSerializer(product).data
    return JsonResponse({'product': productData}, status=200)


@csrf_exempt
def updateProduct(request, product_id):
    product = Products.objects.get(pk=product_id)
    productSerialized = ProductSerializer(product).data
    if request.method == 'POST':
        body = json.loads(request.body)
        product.price= float(body.get('price', product.price))
        product.description =body.get('description', product.description)
        product.quantity= int(body.get('quantity', product.quantity))
        product.save()
        return JsonResponse({'message': 'Product updated successfully'}, status=200)
    return JsonResponse({'product': productSerialized}, status=204)



@login_required
def buyProduct(request, product_id):
    pass