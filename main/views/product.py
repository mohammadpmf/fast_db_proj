from rest_framework import permissions
from rest_framework import viewsets

from main.models.product import Product
from main.serializers.product_serializer import ProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.AllowAny]
