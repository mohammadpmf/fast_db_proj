from rest_framework import viewsets, permissions

from main.models.category import Category
from main.serializers.category_serializer import CategoryReadSerializer, CategoryWriteSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all().select_related('parent').prefetch_related(
        'parent__parent',
        'parent__parent__parent',
        'parent__parent__parent__parent',
        'parent__parent__parent__parent__parent',
        'parent__parent__parent__parent__parent__parent',
    )
    serializer_class = CategoryReadSerializer
    permission_classes = [permissions.AllowAny]

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return CategoryReadSerializer
        return CategoryWriteSerializer
