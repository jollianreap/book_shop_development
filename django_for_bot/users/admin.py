from django.contrib import admin
from .models import User

# Register your models here.
@admin.register(User)
class AdminUser(admin.ModelAdmin):
    list_display = ('username', 'telegram_id', 'is_staff', 'is_active', 'date_joined',)
    search_fields = ('username',)
    ordering = ('username',)