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
        # categoryId = request.POST.get('category')
        print("request.body:", request.body)
        data = json.loads(request.body)
        print("data:", data)
        # category = Category.objects.get(pk=categoryId)
        producer = request.headers.get('X-User-Id')
        category = Category.objects.get(pk=data.get('category_id'))
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