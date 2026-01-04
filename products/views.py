from django.shortcuts import render
from .models import Products


# Create your views here.
def productList(request):
    products = Products.objects.all()
    return render(request, 'products/list.html', {'products': products})

