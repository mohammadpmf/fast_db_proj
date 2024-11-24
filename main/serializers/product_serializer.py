from rest_framework import serializers
from main.models.category import Category
from main.models.product import Product


class ProductReadSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField()

    class Meta:
        model = Product
        fields = ['id', 'title', 'description', 'price', 'extra_info', 'category']
        read_only_fields = ['id', 'category']


class ProductWriteSerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(),
        required=False,
        allow_null=True
    )

    class Meta:
        model = Product
        fields = ['id', 'title', 'description', 'price', 'extra_info', 'category']
        read_only_fields = ['id']
