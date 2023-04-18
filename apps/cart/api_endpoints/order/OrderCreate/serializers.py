from rest_framework.serializers import ModelSerializer

from apps.cart.models import Order, Cart


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

        cart.in_order = True
        cart.save()

        Cart.objects.create(user=user, in_order=False)

        return super().create(validated_data)
