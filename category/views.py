from django.shortcuts import render, redirect
from .models import Category
# from django.contrib.auth.decorators import login_required
# from rest_framework.test import APIClient
from .services import CategoryService
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.

app_name = 'category'


def categoryList(request):
    categories = Category.objects.all()
    return JsonResponse({'items': list(categories.values())})
    # categories = CategoryService.categoryList(request.user)
    # isProducer = CategoryService.canCreateAndModify(request.user)
    # return render(request, 'category/list.html', {'categories': categories, 'allowed': isProducer})

@csrf_exempt
def createCategory(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        Category.objects.create(name=data.get('name'))
        return JsonResponse({'status': 'success'}, status=200)

@csrf_exempt
def deleteCategory(request, category_id):
    if request.method == 'POST':
        category = Category.objects.get(pk=category_id)
        category.delete()
        return JsonResponse({'status': 'success'}, status=200)
