from django.contrib import admin
from .models import Category, Product

# Register your models here.


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    fields = ('name',)
    list_display = ('name',)
    search_fields = ('name',)
    ordering = ('name',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    fields = ('author_name', 'product_name', 'category', 'description',
                    'price', 'quantity')
    list_display = ('author_name', 'product_name', 'category')
    ordering = ('product_name',)
    search_fields = ('author_name', 'product_name')

