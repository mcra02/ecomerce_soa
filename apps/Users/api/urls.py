from django.urls import path
from apps.Users.api.api import UserAPIView
urlpatterns = [
    path('user/',UserAPIView.as_view(), name ='usuario_api')
]
