from django.urls import path, include
from rest_framework_nested import routers
from main.views.category import CategoryViewSet
from main.views.product import ProductViewSet

router = routers.DefaultRouter()
router.register(r'categories', CategoryViewSet, basename='categories')
router.register(r'products', ProductViewSet, basename='products')

urlpatterns = [
    path('', include(router.urls)),
]
