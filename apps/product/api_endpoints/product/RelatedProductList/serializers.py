from django.conf import settings
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from apps.product.models import Product, ProductImages


class RelatedProductListSerializer(ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = (
            'id', 'title', 'image', 'price', 'is_discount', 'discount_price', 'currency_type',
        )

    def get_image(self, obj):
        image = ProductImages.objects.filter(product=obj, use_for_slider=True).first()

        if image is None:
            return ""
        return f"{settings.HOST_URL}{image.image.url}"
