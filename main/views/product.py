from rest_framework import viewsets, permissions

from main.models.product import Product
from main.serializers.product_serializer import (
    ProductReadSerializer,
    ProductWriteSerializer,
)


class ProductViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        """
        Use replica for reads (GET) and master for writes (other methods).
        """
        db = "replica" if self.request.method in ["GET"] else "default"
        return (
            Product.objects.using(db)
            .all()
            .select_related("category")
            .prefetch_related(
                "category__parent",
                "category__parent__parent",
                "category__parent__parent__parent",
                "category__parent__parent__parent__parent",
            )
        )

    def get_serializer_class(self):
        print(self.action)
        if self.action in ["list", "retrieve"]:
            return ProductReadSerializer
        return ProductWriteSerializer
