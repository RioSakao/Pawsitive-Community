# views.py
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from rest_framework.response import Response
import json
from .models import User
from .serializers import UserSerializer
from django.contrib.auth.hashers import check_password


class Login_Views(APIView):
    http_method_names = ['get', 'post']

    @csrf_exempt
    def get(self, request, format=None):
        user_data = User.objects.all()
        serializer = UserSerializer(user_data, many=True)
        return Response(serializer.data)

    @csrf_exempt
    def post(self, request, format=None):
        json_data = next(iter(request.data.keys()))

        # Deserialize the JSON string to a Python object
        data = json.loads(json_data)
        email = data.get('email')
        password = data.get('password')
        try:
            user = User.objects.get(email=email)
            if check_password(password, user.password):
                return user  # Authentication successful
            else:
                return Response(status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response(status=status.HTTP_401_UNAUTHORIZED)


class Sign_UP_Views(APIView):
    http_method_names = ['get', 'post']

    @csrf_exempt
    def get(self, request, format=None):
        user_data = User.objects.all()
        serializer = UserSerializer(user_data, many=True)
        return Response(serializer.data)

    @csrf_exempt
    def post(self, request, format=None):
        # print(request.body.decode('utf-8'))  # Print raw JSON data
        # Get the JSON string from the request body
        json_data = next(iter(request.data.keys()))
        # Deserialize the JSON string to a Python object
        data = json.loads(json_data)
        confirm_password = data.get('confirm_password')
        email = data.get('email')
        password = data.get('password')
        username = data.get('username')
        if password != confirm_password or email is None or username is None:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        User(confirm_password=confirm_password, email=email,
             username=username, password=password).save()
        return Response(status=status.HTTP_201_CREATED)
