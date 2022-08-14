from django.contrib import admin
from django.urls import path

from .views import AuthenticationUserView, CreateUserView

app_name = 'users'

urlpatterns = [
    path('check_user/<int:telegram_id>', AuthenticationUserView.as_view(), name='check_user'),
    path('create_user/', CreateUserView.as_view(), name='create_user')
]