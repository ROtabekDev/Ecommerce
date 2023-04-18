from rest_framework.serializers import ModelSerializer

from apps.cart.models import PaymentType


class PaymentTypeListSerializer(ModelSerializer):
    class Meta:
        model = PaymentType
        fields = ("id", "title")