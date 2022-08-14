from rest_framework.serializers import ModelSerializer
from .models import User


class UserFieldSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('telegram_id', 'username')