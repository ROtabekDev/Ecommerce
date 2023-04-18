from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from apps.user.models import Wishlist


class WishlistListSerializer(ModelSerializer):
    product = serializers.StringRelatedField()

    class Meta:
        model = Wishlist
        fields = ('id', 'product',)