from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import AuthViews

app_name = "authentication"

urlpatterns = [
    # Default DRF token authentication view
    path('create', AuthViews.as_view()),
]
