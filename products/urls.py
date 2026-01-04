from django.urls import path
from .views import *

app_name ='products'

urlpatterns = [
    path('', productList, name='products'),
    path('create/', createProduct, name='createProduct'),
    path('delete/<int:product_id>/', deleteProduct, name='deleteProduct'),
]