from rest_framework import serializers
from main.models.category import Category


class CategoryReadSerializer(serializers.ModelSerializer):
    parent = serializers.StringRelatedField()

    class Meta:
        model = Category
        fields = ['id', 'title', 'description', 'parent']
        read_only_fields = ['id', 'parent']
        '''آی دی که خودش رید آنلی هست. یه چیزی رو هم وقتی
        استرینگ ریلیتد فیلد تعریف میکنیم
        رید آنلی میشه. اما نوشتم که واضح تر باشه.'''


class CategoryWriteSerializer(serializers.ModelSerializer):
    parent = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(),
        required=False,
        allow_null=True
    )

    class Meta:
        model = Category
        fields = ['id', 'title', 'description', 'parent']
        read_only_fields = ['id']
