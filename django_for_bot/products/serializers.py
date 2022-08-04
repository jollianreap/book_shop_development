from rest_framework.serializers import ModelSerializer
from .models import Category, Product


class ProductFieldSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = ("product_name", "price", "category")

