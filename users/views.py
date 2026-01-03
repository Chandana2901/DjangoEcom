from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Users

# Create your views here.
app_name = 'users'

def createUser(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        phoneNumber = request.POST.get('phoneNumber')
        address = request.POST.get('address')
        role = request.POST.get('role', 'consumer')
        Users.objects.create_user(name=name, email=email, password=password, phoneNumber=phoneNumber, address=address, role=role)
        return redirect('category:categories')
    return render(request, 'users/signup.html')

    