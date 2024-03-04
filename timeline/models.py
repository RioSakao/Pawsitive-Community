from django.db import models


class Timeline(models.Model):
    username = models.CharField(max_length=255)
    missing = models.BooleanField(default=False)
    foster = models.BooleanField(default=False)
    adoption = models.BooleanField(default=False)
    general = models.BooleanField(default=False)
    content = models.TextField()
    images = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)


timeline = Timeline('riosakao', 'general', 'test', '')
