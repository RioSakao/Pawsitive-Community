from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Timeline
from .serializers import TimelineSerializer


class TimelineViews(APIView):
    http_method_names = ['get', 'post']

    def get(self, request, format=None):
        timeline = Timeline.objects.all()
        serializer = TimelineSerializer(timeline, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        p_username = str(request.data.get('username'))
        p_category = str(request.data.get('category'))
        p_comment = str(request.data.get('comment'))
        p_image = str(request.data.get('images'))
        Timeline(username=p_username, category=p_category,
                 comment=p_comment, images=p_comment).save()
        return Response(status=status.HTTP_201_CREATED)
