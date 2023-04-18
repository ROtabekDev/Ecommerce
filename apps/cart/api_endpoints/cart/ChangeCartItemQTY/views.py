from rest_framework.generics import CreateAPIView
from rest_framework.response import Response

from .serializers import ChangeCartItemQTYSerializer


class ChangeCartItemQTYAPIView(CreateAPIView):
    serializer_class = ChangeCartItemQTYSerializer

    def create(self, request, *args, **kwargs):
        super().create(request, *args, **kwargs)
        return Response({"status": 202, "message": "The count of products has been changed successfully."})