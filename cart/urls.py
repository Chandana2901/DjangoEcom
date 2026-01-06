from django.urls import path
from .views import *


app_name = 'cart'

urlpatterns = [
    path('', viewCart, name='viewCart'),
    path('add/<int:product_id>/', addToCart, name='addToCart' )
]