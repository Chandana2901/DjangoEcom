from django.shortcuts import render, redirect
from .models import Category
# from django.contrib.auth.decorators import login_required
# from rest_framework.test import APIClient
from .services import CategoryService


# Create your views here.

app_name = 'category'

def categoryList(request):
    categories = CategoryService.categoryList(request.user)
    isProducer = CategoryService.canCreateAndModify(request.user)
    return render(request, 'category/list.html', {'categories': categories, 'allowed': isProducer})

def createCategory(request):
    if request.method == 'POST':
        data = {
            'name': request.POST.get('name')
        }
        CategoryService.createCategory(request.user, data)
        return redirect('category:categories')

def deleteCategory(request, category_id):
    if request.method == 'POST':
        category = Category.objects.get(pk=category_id)
        CategoryService.deleteCategory(request.user, category)
        return redirect('category:categories')
