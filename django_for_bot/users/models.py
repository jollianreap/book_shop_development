from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    telegram_id = models.PositiveIntegerField(verbose_name='Telegram user id', unique=True, null=False)
    REQUIRED_FIELDS = ['telegram_id', 'username']

    def __str__(self):
        return f'#{self.telegram_id} | {self.username}'
