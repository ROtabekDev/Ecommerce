from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny

from .serializers import ContactCreateSerializer


class ContanctCreateAPIView(CreateAPIView):
    serializer_class = ContactCreateSerializer
    permission_classes = (AllowAny,)