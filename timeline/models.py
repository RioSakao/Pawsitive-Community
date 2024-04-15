from django.db import models
# from authentication.models import User


class Timeline(models.Model):
    username = models.CharField(max_length=255)
    missing = models.BooleanField(default=False)
    foster = models.BooleanField(default=False)
    adoption = models.BooleanField(default=False)
    general = models.BooleanField(default=False)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)


class Comment(models.Model):
    post = models.ForeignKey(Timeline, on_delete=models.CASCADE)
    username = models.CharField(max_length=255, default="")
    text = models.TextField()


class Image(models.Model):
    timeline = models.ForeignKey(
        Timeline, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='timeline_image')

    def __str__(self):
        return str(self.image)
