from rest_framework.serializers import ModelSerializer
from .models import Category, Product


class ProductFieldSerializer(ModelSerializer):

    class Meta:
        model = Product
        fields = "__all__"


class CategoryFieldSerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"