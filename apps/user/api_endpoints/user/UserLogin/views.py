from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny

from .serializers import LoginSerializer


class UserLoginAPIView(CreateAPIView):
    serializer_class = LoginSerializer
    permission_classes = (AllowAny,)

    def perform_create(self, serializer):
        pass