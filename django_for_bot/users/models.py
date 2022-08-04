from django.db import models
from django.contrib.auth.models import AbstractUser, AbstractBaseUser

# Create your models here.


class AdminUser(AbstractUser):  # Special model for admins
    telegram_id = models.PositiveIntegerField(verbose_name='Telegram user id', unique=True, null=False)

    REQUIRED_FIELDS = ('telegram_id', )

    def __str__(self):
        return f'#{self.telegram_id} | {self.username}'


class User(AbstractBaseUser):  # Model for ordinary users

    telegram_id = models.PositiveIntegerField(verbose_name="Telegram user id", unique=True,
                                              blank=False, primary_key=True)
    username = models.CharField(verbose_name='Telegram username', max_length=60)
    created_at = models.DateTimeField(verbose_name='Time of creation', auto_now_add=True)

    USERNAME_FIELD = 'telegram_id'

    class Meta:
        verbose_name_plural = "OrdinaryUsers"

    def __str__(self):
        return f'#{self.telegram_id} | {self.username}'
