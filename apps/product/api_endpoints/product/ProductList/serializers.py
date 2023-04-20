from django.conf import settings
from django.db.models import Sum
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from apps.product.models import Product, ProductImages, Review


class ProductListSerializer(ModelSerializer):
    image = serializers.SerializerMethodField()
    product_rating_number = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = (
            'id', 'title', 'image', 'product_rating_number', 'price', 'is_discount', 'discount_price', 'currency_type',
            'description'
        )

    def get_image(self, obj):
        image = ProductImages.objects.filter(product=obj, use_for_slider=True).first()

        if image is None:
            return ""
        return f"{settings.HOST_URL}{image.image.url}"

    def get_product_rating_number(self, obj):
        count_rating_number = Review.objects.filter(product=obj).count()
        sum_rating_number = Review.objects.filter(product=obj).aggregate(Sum('rating_number'))['rating_number__sum']

        if sum_rating_number is None:
            sum_rating_number = 0

        if count_rating_number is None:
            count_rating_number = 0

        try:
            rating_number = sum_rating_number / count_rating_number
        except ZeroDivisionError:
            rating_number = 0

        rating_number = round(rating_number, 1)

        return rating_number
