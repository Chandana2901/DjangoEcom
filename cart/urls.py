from django.urls import path
from .views import *


app_name = 'cart'

urlpatterns = [
    path('list/', viewCart, name='viewCart'),
    path('add/<int:product_id>/', addToCart, name='addToCart' )
]