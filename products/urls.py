from django.urls import path
from .views import *

app_name ='products'

urlpatterns = [
    path('list/', productList, name='products'),
    path('create/', createProduct, name='createProduct'),
    path('get/<int:product_id>/', getProduct, name='getProduct'),
    path('delete/<int:product_id>/', deleteProduct, name='deleteProduct'),
    path('update/<int:product_id>/', updateProduct, name="updateProduct")
]