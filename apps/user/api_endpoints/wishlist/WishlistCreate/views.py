from rest_framework.generics import CreateAPIView

from .serializers import WishlistCreateSerializer


class WishlistCreateAPIView(CreateAPIView):
    serializer_class = WishlistCreateSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)