from django.urls import path
from .views import TimelineViews, CommentViews

app_name = "timeline"

urlpatterns = [
    path('timeline', TimelineViews.as_view()),
    path('timeline/comments', CommentViews.as_view()),
]
