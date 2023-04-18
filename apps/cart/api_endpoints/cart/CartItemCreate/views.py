from rest_framework.generics import CreateAPIView
from rest_framework.response import Response

from .serializers import CartItemCreateSerializer


class CartItemCreateAPIView(CreateAPIView):
    serializer_class = CartItemCreateSerializer

    def create(self, request, *args, **kwargs):
        super().create(request, *args, **kwargs)
        return Response({"status": 200, "message": "The product has been added to the cart."})