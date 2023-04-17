from django.urls import path  # noqa: F401

from apps.user.api_endpoints.user import UserRegisterAPIView, UserLoginAPIView

urlpatterns = [
    path('register/', UserRegisterAPIView.as_view(), name='user-register'),
    path('login/', UserLoginAPIView.as_view(), name='user-login'),
]
