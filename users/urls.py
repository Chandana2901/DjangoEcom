from django.urls import path
from .views import *


app_name = 'users'

urlpatterns = [
    path('signup/', createUser, name='signup'),
    path('login/', loginUser, name='login'),
    path('logout/', logoutUser, name='logout')
]