from django.http import Http404
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer


from apps.cart.utils import update_cart
from apps.cart.models import CartItem, Cart, CartProduct
from apps.product.models import Product


class CartItemCreateSerializer(ModelSerializer):
    product_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = CartItem
        fields = ("product_id",)

    def create(self, validated_data):

        try:
            product = Product.objects.get(id=validated_data["product_id"])
        except Product.DoesNotExist:
            raise Http404("Product not found")

        user = self.context["request"].user

        cart = Cart.objects.filter(user=user, in_order=False).first()

        cart_item, created = CartItem.objects.get_or_create(
            cart=cart, product=product
        )

        if created:
            CartProduct.objects.create(cart=cart, product=cart_item)

        update_cart(cart=cart)

        return cart_item