from django.urls import path
from .views import TimelineViews

app_name = "timeline"

urlpatterns = [
    path('timeline', TimelineViews.as_view()),
]
