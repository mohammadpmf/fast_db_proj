from django.contrib import admin

from main.models.category import Category
from main.models.product import Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'parent']
    list_display_links = ['id', 'title', 'description', 'parent']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'category' ,'title' ,'description' ,'price' ,'extra_info']
    list_display_links = ['id', 'category' ,'title' ,'description' ,'price' ,'extra_info']
