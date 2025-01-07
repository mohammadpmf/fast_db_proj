from rest_framework import viewsets, permissions

from main.models.category import Category
from main.serializers.category_serializer import (
    CategoryReadSerializer,
    CategoryWriteSerializer,
)


class CategoryViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        """
        Use replica for reads (GET) and master for writes (other methods).
        """
        db = "replica" if self.request.method in ["GET"] else "default"
        return (
            Category.objects.using(db)
            .all()
            .select_related("parent")
            .prefetch_related(
                "parent__parent",
                "parent__parent__parent",
                "parent__parent__parent__parent",
                "parent__parent__parent__parent__parent",
                "parent__parent__parent__parent__parent__parent",
            )
        )

    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return CategoryReadSerializer
        return CategoryWriteSerializer

    # # Inside your viewset methods if needed (optional override)
    # def perform_create(self, serializer):
    #     """
    #     Save the object using the default (master) database.
    #     """
    #     serializer.save(using='default')

    # def perform_update(self, serializer):
    #     """
    #     Update the object using the default (master) database.
    #     """
    #     serializer.save(using='default')

    # def perform_destroy(self, instance):
    #     """
    #     Delete the object using the default (master) database.
    #     """
    #     instance.delete(using='default')
