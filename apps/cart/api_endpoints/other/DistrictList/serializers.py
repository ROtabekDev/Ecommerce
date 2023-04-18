from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from apps.cart.models import District


class DistrictListSerializer(ModelSerializer):
    region = serializers.StringRelatedField()

    class Meta:
        model = District
        fields = ('id', 'title', 'region')
