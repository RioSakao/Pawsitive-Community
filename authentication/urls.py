from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import Sign_UP_Views, Login_Views

app_name = "authentication"

urlpatterns = [
    # Default DRF token authentication view
    path('create', Sign_UP_Views.as_view()),
    path('login', Login_Views.as_view()),
]
