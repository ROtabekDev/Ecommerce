from django.conf import settings
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from apps.cart.models import CartItem
from apps.product.models import Product, ProductImages


class ProductMiniSerializer(ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ('title', 'image')

    def get_image(self, obj):
        image = ProductImages.objects.filter(product=obj, use_for_slider=True).first()

        if image is None:
            return ""
        return f"{settings.HOST_URL}{image.image.url}"

    # def to_representation(self, instance):
    #     representation = super().to_representation(instance)
    #
    #     image = ProductImages.objects.filter(product=instance, use_for_slider=True)
    #
    #     if image.exists():
    #         serializer = ProductImagesSerializer(image, context={"request": self.context["request"]})
    #         representation["image"] = serializer.data
    #
    #     return representation


class CartItemListSerializer(ModelSerializer):
    product = ProductMiniSerializer()

    class Meta:
        model = CartItem
        fields = ('product', 'qty', 'final_price')

