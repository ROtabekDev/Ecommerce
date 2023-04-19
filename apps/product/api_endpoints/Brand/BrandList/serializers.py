from rest_framework import serializers

from apps.product.models import Brand


class BrandListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ('id', 'title', 'slug', 'logo')
