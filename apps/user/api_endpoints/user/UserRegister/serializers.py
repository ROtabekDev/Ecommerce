from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from apps.cart.models import Cart
from apps.user.models import User


class RegisterSerializer(ModelSerializer):
    password = serializers.CharField(min_length=6, max_length=68, write_only=True)
    password2 = serializers.CharField(min_length=6, max_length=68, write_only=True)
    token = serializers.DictField(source="tokens", read_only=True)

    class Meta:
        model = User
        fields = ("id", "first_name", "last_name", "phone_number", "password", "password2", "token")

    def validate(self, attrs):
        password = attrs.get("password")
        password2 = attrs.pop("password2")

        if password != password2:
            raise serializers.ValidationError({"success": False, "message": "Parollar bir xil emas."})

        del password2

        return attrs

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        Cart.objects.create(user=user, in_order=False)
        return user