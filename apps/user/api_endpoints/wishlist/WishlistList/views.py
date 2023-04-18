from rest_framework.generics import ListAPIView

from apps.user.models import Wishlist

from .serializers import WishlistListSerializer


class WishlistListAPIView(ListAPIView):
    serializer_class = WishlistListSerializer

    def get_queryset(self):
        queryset = Wishlist.objects.filter(user=self.request.user)
        return queryset