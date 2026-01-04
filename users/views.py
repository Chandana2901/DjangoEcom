from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Users
from django.contrib.auth import authenticate, login, logout

# Create your views here.
app_name = 'users'

def createUser(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        phoneNumber = request.POST.get('phoneNumber')
        address = request.POST.get('address')
        role = request.POST.get('role', 'Consumer')
        Users.objects.create_user(name=name, email=email, password=password, phoneNumber=phoneNumber, address=address, role=role)
        return redirect('category:categories')
    return render(request, 'users/signup.html')

def loginUser(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            user = Users.objects.get(email=email)
            if user.check_password(password):
                auth = authenticate(request, email=email, password=password)
                if auth is not None:
                    login(request, auth)
                    return redirect('category:categories')
                else:
                    return HttpResponse("Authentication failed")
            else:
                return HttpResponse("Invalid password")
        except Users.DoesNotExist:
            return HttpResponse("User does not exist")
    return render(request, 'users/login.html')


def logoutUser(request):
    logout(request)
    return redirect('category:categories')