from django.contrib import admin
from django.urls import path
from .views import AllProductView, FilterProductByCategoryView, FilterProductByNameView, AllProductView, ALlCategoryView

app_name = 'products'

urlpatterns = [
    path('all_books/', AllProductView.as_view(), name='all_books'),
    path('all_category/', ALlCategoryView.as_view(), name='all_category'),
    path('filter_category/<str:category>/', FilterProductByCategoryView.as_view(), name='filter_by_category'),
    path('filter_id/<int:id>/', FilterProductByNameView.as_view(), name='filter_by_id'),
]