from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Timeline
from .serializers import TimelineSerializer
from django.views.decorators.csrf import csrf_exempt
import json


class TimelineViews(APIView):
    http_method_names = ['get', 'post']

    @csrf_exempt
    def get(self, request, format=None):
        timeline = Timeline.objects.all()
        serializer = TimelineSerializer(timeline, many=True)
        return Response(serializer.data)

    @csrf_exempt
    def post(self, request, format=None):
        # print(request.body.decode('utf-8'))  # Print raw JSON data
        # Get the JSON string from the request body
        json_data = next(iter(request.data.keys()))

        # Deserialize the JSON string to a Python object
        data = json.loads(json_data)

        # Access the properties from the Python object
        p_username = data.get('username', '')
        p_categories = data.get('categories', {})
        p_comment = data.get('comment', '')
        p_image = data.get('image', '')
        if p_categories is not None:
            missing = p_categories.get('missing', False)
            foster = p_categories.get('foster', False)
            adoption = p_categories.get('adoption', False)
            general = p_categories.get('general', False)
            Timeline(username=p_username, missing=missing, foster=foster,
                     adoption=adoption, general=general,
                     comment=p_comment, images=p_image
                     ).save()
        return Response(status=status.HTTP_201_CREATED)
