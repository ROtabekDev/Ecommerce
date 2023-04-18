from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from apps.cart.models import Cart


class CartDetailSerializer(ModelSerializer):
    user = serializers.StringRelatedField()

    class Meta:
        model = Cart
        fields = ('id', 'user', 'total_products', 'final_price', 'shipping_cost')