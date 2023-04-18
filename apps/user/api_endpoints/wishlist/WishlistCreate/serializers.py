from rest_framework.serializers import ModelSerializer

from apps.user.models import Wishlist


class WishlistCreateSerializer(ModelSerializer):

    class Meta:
        model = Wishlist
        fields = ('product',)
        read_only_fields = ('user',)