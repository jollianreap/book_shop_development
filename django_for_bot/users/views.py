from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.views import Response

from .serializers import UserFieldSerializer
from .models import User
# Create your views here.


class AuthenticationUserView(APIView):
    def get(self, *args, **kwargs):

        try:
            User.objects.get(telegram_id=kwargs['telegram_id'])
            return Response(status=200, data={'success': True})

        except:
            return Response(status=500, data={'success': False})


class CreateUserView(APIView):
    def post(self, request, format=None):
        serializer = UserFieldSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        else:
            return Response(serializer.errors)
