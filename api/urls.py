from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import CategoryViewSet #CategoryListCreateApiView #categoryList

router = DefaultRouter()
router.register("categories", CategoryViewSet)

# urlpatterns = [
#     # path('categories/', categoryList)
#     path('categories/', CategoryListCreateApiView.as_view())
# ]
urlpatterns = router.urls

