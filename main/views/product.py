from rest_framework import permissions
from rest_framework import viewsets

from main.models.product import Product
from main.serializers.product_serializer import ProductReadSerializer, ProductWriteSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all().select_related('category').prefetch_related(
        'category__parent',
        'category__parent__parent',
        'category__parent__parent__parent',
        'category__parent__parent__parent__parent',
        )
    permission_classes = [permissions.AllowAny]
    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return ProductReadSerializer
        return ProductWriteSerializer
