from django.contrib import admin
from django.urls import path
from .views import AllProductView, FilterProductByCategoryView, FilteProductByNameView

app_name = 'products'

urlpatterns = [
    path('all/', AllProductView.as_view(), name='all'),
    path('filter_category/<str:category>/', FilterProductByCategoryView.as_view(), name='filter_by_category'),
    path('filter_name/<str:name>/', FilteProductByNameView.as_view(), name='filter_by_name')
]