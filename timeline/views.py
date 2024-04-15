from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Timeline, Comment, Image
from .serializers import TimelineSerializer, CommentSerializer
from django.views.decorators.csrf import csrf_exempt
import json


class CommentViews(APIView):
    http_method_names = ['get', 'post']
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    @csrf_exempt
    def post(self, request, format=None):
        json_data = next(iter(request.data.keys()))
        # Deserialize the JSON string to a Python object
        data = json.loads(json_data)
        post_id = data.get('id')
        username = data.get('username')
        print(post_id)
        try:
            post = Timeline.objects.get(pk=post_id)
            text = data.get('text')
            print(text)
            Comment(post=post, text=text, username=username).save()
        except:
            print("Catched an error")

        return Response(status=status.HTTP_201_CREATED)

    @csrf_exempt
    def get(self, request, format=None):
        comments = Comment.objects.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)


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
        p_content = data.get('content', '')
        # image_data = data.get('image')
        p_image = None
        # if image_data is not None:
        #     p_image = Image.objects.create(**image_data)
        if p_categories is not None:
            missing = p_categories.get('missing', False)
            foster = p_categories.get('foster', False)
            adoption = p_categories.get('adoption', False)
            general = p_categories.get('general', False)
            timeline_instance = Timeline.objects.create(
                username=p_username,
                missing=missing,
                foster=foster,
                adoption=adoption,
                general=general,
                content=p_content)
            if p_image is not None:
                timeline_instance.images.set(p_image)
            timeline_instance.save()
            # Timeline(username=p_username, missing=missing, foster=foster,
            #          adoption=adoption, general=general,
            #          content=p_content, images=p_image
            #          ).save()
        return Response(status=status.HTTP_201_CREATED)
