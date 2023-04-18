from django.shortcuts import get_object_or_404
from rest_framework.generics import RetrieveAPIView

from .serializers import CartDetailSerializer

from apps.cart.models import Cart


class CartDetailAPIView(RetrieveAPIView):
    serializer_class = CartDetailSerializer

    def get_queryset(self):
        return Cart.objects.filter(user=self.request.user, in_order=False)

    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(queryset)
        return obj