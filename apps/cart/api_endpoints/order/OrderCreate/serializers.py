from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from apps.cart.models import Order, Cart, CartItem
from apps.user.models import PurchasedProduct
from apps.product.models import Product


class OrderCreateSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = (
            "cart",
            "first_name",
            "last_name",
            "phone_number",
            "buying_type",
            "region",
            "district",
            "home_address",
            "payment_type",
        )

        read_only_fields = ("user",)

    def create(self, validated_data):
        user = self.context["request"].user

        cart = validated_data["cart"]

        try:
            cart = Cart.objects.get(id=cart.id, user=user)
        except Product.DoesNotExist:
            raise Http404("Cart not found")

        if cart.in_order != False:
            raise serializers.ValidationError({"message": "This cart has been ordered."})

        cart_items = CartItem.objects.filter(cart=cart).values('product', 'qty')

        for cart_item in cart_items:
            product_id = cart_item.get('product')
            qty = cart_item.get('qty')
            product = Product.objects.get(id=product_id)
            purchased_product = PurchasedProduct.objects.get_or_create(user=user, product=product)
            purchased_product[0].qty += qty
            purchased_product[0].save()

        cart.in_order = True
        cart.save()

        Cart.objects.create(user=user, in_order=False)

        return super().create(validated_data)
