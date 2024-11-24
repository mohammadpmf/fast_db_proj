from django.contrib import admin

from main.models.category import Category
from main.models.product import Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'parent']
    list_display_links = ['id', 'title', 'description', 'parent']

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        return queryset.select_related('parent').prefetch_related(
            'parent__parent',  # 2nd layer
            'parent__parent__parent',  # 3rd layer
            'parent__parent__parent__parent',  # 4th layer, if necessary
            'parent__parent__parent__parent__parent',  # 5th layer, if necessary
        )
    
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'category' ,'title' ,'description' ,'price' ,'extra_info']
    list_display_links = ['id', 'category' ,'title' ,'description' ,'price' ,'extra_info']

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        return queryset.select_related('category').prefetch_related(
            'category__parent',  # 2nd layer
            'category__parent__parent',  # 3rd layer
            'category__parent__parent__parent',  # 4th layer, if necessary
            'category__parent__parent__parent__parent',  # 5th layer, if necessary
        )
