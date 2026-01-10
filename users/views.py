from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Users
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

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

@csrf_exempt
def loginUser(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        email = data.get('email')
        password = data.get('password')
        try:
            user = Users.objects.get(email=email)
            if user.check_password(password):
                auth = authenticate(request, email=email, password=password)
                if auth is not None:
                    login(request, auth)
                    return JsonResponse({'message': 'Login successful', 'user_id': user.id}, status=200)
                else:
                    return JsonResponse({'error': 'Authentication failed'}, status=401)
            else:
                return HttpResponse("Invalid password", status=401)
        except Users.DoesNotExist:
            return JsonResponse({'error': 'User does not exist'}, status=404)


def logoutUser(request):
    logout(request)
    return redirect('categories')