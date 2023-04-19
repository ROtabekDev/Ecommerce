from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from django.db.models import Sum

from apps.product.models import Product, ProductImages, Review
from apps.user.models import PurchasedProduct


class ProductImagesSerializer(ModelSerializer):
    class Meta:
        model = ProductImages
        fields = ('image', 'use_for_slider')


class ProductDetailSerializer(ModelSerializer):
    brand = serializers.StringRelatedField()
    images = serializers.SerializerMethodField()
    reviews_count = serializers.SerializerMethodField()
    count_products_sold = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = (
            'title', 'brand', 'price', 'is_discount', 'discount_price', 'currency_type', 'available', 'reviews_count',
            'count_products_sold', 'images'
        )

    def get_images(self, obj):
        images = ProductImages.objects.filter(product=obj)
        serializer = ProductImagesSerializer(images, many=True, context={'request': self.context['request']})
        data = serializer.data
        return data

    def get_reviews_count(self, obj):
        reviews_count = Review.objects.filter(product=obj).count()
        return reviews_count

    def get_count_products_sold(self, obj):
        count_products_sold = PurchasedProduct.objects.filter(product=obj).aggregate(Sum("qty"))['qty__sum']
        return count_products_sold
