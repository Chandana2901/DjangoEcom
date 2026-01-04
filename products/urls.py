from django.urls import path
from .views import productList

app_name ='products'

urlpatterns = [
    path('', productList, name='products')
]