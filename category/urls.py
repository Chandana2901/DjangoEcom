from django.urls import path
from .views import *

urlpatterns = [
    path('', categoryList, name='categories'),
    path('create/', createCategory, name='createCategory'),
    path('delete/<int:category_id>/', deleteCategory, name='deleteCategory')
]
