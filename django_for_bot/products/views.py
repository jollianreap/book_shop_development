from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Category, Product
from .serializers import ProductFieldSerializer, CategoryFieldSerializer
# Create your views here.


class AllProductView(APIView):
    def get(self, *args, **kwargs):
        books = Product.objects.all()
        serialized_data = ProductFieldSerializer(books, many=True)
        return Response(serialized_data.data)


class ALlCategoryView(APIView):
    def get(self, *args, **kwargs):
        categories = Category.objects.all()
        serialized_data = CategoryFieldSerializer(categories, many=True)
        return Response(serialized_data.data)


class FilterProductByCategoryView(APIView):
    def get(self, *args, **kwargs):
        filter_data = Product.objects.filter(category=kwargs["category"])
        serialized_data = ProductFieldSerializer(filter_data, many=True)
        return Response(serialized_data.data)


class FilterProductByNameView(APIView):
    def get(self, *args, **kwargs):
        filter_data = Product.objects.filter(id=kwargs["id"])
        serialized_data = ProductFieldSerializer(filter_data, many=True)
        return Response(serialized_data.data)


