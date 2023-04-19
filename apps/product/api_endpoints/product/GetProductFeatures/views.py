from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny

from .serializers import FeatureListSerializer

from apps.product.models import Product, Feature


class GetProductFeaturesListAPIView(ListAPIView):
    serializer_class = FeatureListSerializer
    permission_classes = (AllowAny,)

    def get_queryset(self):
        features = Feature.objects.filter(product=self.kwargs['product_id'])
        return features