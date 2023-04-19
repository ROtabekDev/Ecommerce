from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from apps.product.models import Review


class ReviewListSerializer(ModelSerializer):
    product = serializers.StringRelatedField()

    class Meta:
        model = Review
        fields = ('id', 'product', 'rating_number', 'text')