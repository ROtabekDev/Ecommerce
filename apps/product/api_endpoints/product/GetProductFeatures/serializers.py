from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from apps.product.models import Feature, FeatureName


class FeatureListSerializer(ModelSerializer):
    feature_name = serializers.StringRelatedField()

    class Meta:
        model = Feature
        fields = ('feature_name', 'value')