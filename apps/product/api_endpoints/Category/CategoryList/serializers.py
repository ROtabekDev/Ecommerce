from rest_framework import serializers

from apps.product.models import Category


class CategoryListSerializer(serializers.ModelSerializer):
    parent = serializers.StringRelatedField()

    class Meta:
        model = Category
        fields = ("id", "title", "slug", "logo", "parent")
