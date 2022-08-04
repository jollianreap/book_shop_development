from django.contrib import admin
from .models import User, AdminUser

# Register your models here.


@admin.register(AdminUser)
class AdminUser(admin.ModelAdmin):
    list_display = ('username', 'telegram_id', 'is_staff', 'is_active', 'date_joined',)
    search_fields = ('username',)
    readonly_fields = ('telegram_id', 'date_joined')
    ordering = ('username',)


@admin.register(User)
class AdminOrdinaryUser(admin.ModelAdmin):
    list_display = ('telegram_id', 'username', 'created_at')
    search_fields = ('username',)
    readonly_fields = ('telegram_id', 'created_at')
    ordering = ('username', )
