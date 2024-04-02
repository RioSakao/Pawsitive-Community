from rest_framework import serializers
from .models import Timeline, Comment, Image


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['id', 'timeline', 'image']


class TimelineSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)
    images = ImageSerializer(many=True, read_only=True)

    class Meta:
        model = Timeline
        fields = ['id', 'username', 'missing', 'foster',
                  'adoption', 'general', 'content',
                  'images', 'comments', 'created_at']
