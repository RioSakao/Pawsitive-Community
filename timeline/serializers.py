from rest_framework import serializers
from .models import Timeline


class TimelineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Timeline
        fields = ['id', 'username', 'missing', 'foster',
                  'adoption', 'general', 'content', 'images', 'created_at']
