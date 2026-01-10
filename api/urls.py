from django.urls import path, include
from .views import GatewayProxyApi
# from rest_framework.routers import DefaultRouter

# from .views import CategoryViewSet, userCapabilities #CategoryListCreateApiView #categoryList

# router = DefaultRouter()
# router.register("categories", CategoryViewSet)

# urlpatterns = [
#     # path('categories/', categoryList)
#     path('categories/', CategoryListCreateApiView.as_view())
# ]
# urlpatterns = router.urls

# urlpatterns += [
#     path('capabilities/', userCapabilities, name='userCapabilities')
# ]

from .views import *

# app_name='gateway-proxy'
urlpatterns = [
    path('api/gateway/<str:service>/<path:path>', GatewayProxyApi.as_view(), name='gateway-proxy'),
    path('login/', loginUser, name='login'),
    path('logout/', logoutUser, name='logoutGateway'),
    path('createCategory/', createCategory, name='createCategory'),
    path('deleteCategory/<int:category_id>/', deleteCategory, name='deleteCategory'),
    path('products/', productList, name='products'),
    path('productsCreate/', createProductView, name='productsCreate'),
    path('productsCreateSubmit/', createProduct, name='productsCreateSubmit'),
    path('productsDelete/<int:product_id>/', deleteProduct, name='productsDelete'),
    path('categories/', categoryList, name='categories'),
]