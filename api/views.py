# # from rest_framework import viewsets
# # from category.models import Category
# # from .serializers import CategorySerializer

# # # Create your views here.

# # class CategoryViewSet(viewsets.ModelViewSet):
# #     queryset = Category.objects.all()
# #     serializer_class = CategorySerializer


# # from rest_framework.decorators import api_view
# # from rest_framework.response import Response
# # from rest_framework import status
# # from rest_framework.generics import ListCreateAPIView
# from rest_framework.viewsets import ModelViewSet
# # from rest_framework.permissions import IsAuthenticatedOrReadOnly
# from category.models import Category
# from .serializers import CategorySerializer
# from .permissions import IsProducerOrReadOnly
# from rest_framework.decorators import api_view, permission_classes
# from rest_framework.permissions import IsAuthenticated
# from rest_framework.response import Response

# # @api_view(['GET'])
# # def categoryList(request):
# #     categories = Category.objects.all()
# #     serializer = CategorySerializer(categories, many=True)
# #     return Response(serializer.data)

# # class CategoryListCreateApiView(ListCreateAPIView):
# #     queryset = Category.objects.all()
# #     serializer_class = CategorySerializer

# class CategoryViewSet(ModelViewSet):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer
#     permission_classes = [IsProducerOrReadOnly]


# @api_view(['GET'])
# @permission_classes([IsAuthenticated])
# def userCapabilities(request):
#     isProducer = request.user.role == 'Producer'
    
#     return Response({
#         "categories":{
#             "can_create": isProducer,
#             "can_delete": isProducer,
#         }
#     })


from .permissions import GatewayProxyApi
from django.shortcuts import render, redirect

def productList(request):
    gateway = GatewayProxyApi()
    response = gateway.get(request, service='product', path='')
    data = response.json()
    
    return render(request, 'products/list.html', {
        'products': data.get('items', []),
        'allowed': data.get('_ui_permissions',{}).get('can_create', False),
        'role': data.get('_ui_permissions', {}).get('role_label')
        })

