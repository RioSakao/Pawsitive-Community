from django.db import models


class Timeline(models.Model):
    username = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    comment = models.CharField(max_length=255)
    images = models.ImageField(
        upload_to='../Images')


timeline = Timeline('riosakao', 'general', 'test', '')
