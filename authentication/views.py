# views.py
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from rest_framework.response import Response
import json
from .models import User
from .serializers import UserSerializer


class AuthViews(APIView):
    http_method_names = ['get', 'post']

    @csrf_exempt
    def get(self, request, format=None):
        timeline = User.objects.all()
        serializer = UserSerializer(timeline, many=True)
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

        print(confirm_password)
        print(password)
        print(username)
        print(email)
        # Check if CSRF token is present in the request headers and validate it
        # if not request.COOKIES.get('csrftoken') or not request.headers.get('X-CSRFToken'):
        #     return Response({'error': 'CSRF token not set'}, status=status.HTTP_403_FORBIDDEN)
        # if request.COOKIES['csrftoken'] != request.headers['X-CSRFToken']:
        #     return Response({'error': 'CSRF token mismatch'}, status=status.HTTP_403_FORBIDDEN)
        if password != confirm_password or email is None or username is None:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        User(confirm_password=confirm_password, email=email,
             username=username, password=password).save()
        return Response(status=status.HTTP_201_CREATED)
