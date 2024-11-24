from rest_framework import permissions
from rest_framework import viewsets

from main.models.category import Category
from main.serializers.category_serializer import CategorySerializer


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.AllowAny]
