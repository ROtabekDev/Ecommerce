from django.http import Http404
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from apps.product.models import Product
from apps.cart.models import CartItem, Cart
from apps.cart.utils import update_cart


class ChangeCartItemQTYSerializer(ModelSerializer):
    product_id = serializers.IntegerField(write_only=True)
    qty = serializers.IntegerField(write_only=True)

    class Meta:
        model = CartItem
        fields = ("product_id", "qty")

    def create(self, validated_data):

        try:
            product = Product.objects.get(id=validated_data["product_id"])
        except Product.DoesNotExist:
            raise Http404("Product not found")

        user = self.context["request"].user

        cart = Cart.objects.filter(user=user, in_order=False).first()

        try:
            cart_item = CartItem.objects.get(cart=cart, product=product)
            cart_item.qty = validated_data["qty"]
            cart_item.save()
        except CartItem.DoesNotExist:
            raise Http404("CartItem not found")

        update_cart(cart=cart)

        return cart_item