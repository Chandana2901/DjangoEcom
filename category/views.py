from django.shortcuts import render, redirect
from .models import Category

# Create your views here.

app_name = 'category'

def categoryList(request):
    categories = Category.objects.all()
    return render(request, 'category/list.html', {'categories': categories})

def createCategory(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        Category.objects.create(name=name)
        return redirect('category:categories')

def deleteCategory(request, category_id):
    if request.method == 'POST':
        category = Category.objects.filter(pk=category_id)
        category.delete()
        return redirect('category:categories')
