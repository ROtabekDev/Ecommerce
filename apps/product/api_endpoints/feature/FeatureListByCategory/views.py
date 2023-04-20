from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny
from .serializer import FeatureListByCategorySerializer
from apps.product.models import Feature, Product


class FeatureListByCategoryListAPIView(ListAPIView):
    serializer_class = FeatureListByCategorySerializer
    permission_classes = (AllowAny,)

    def get_queryset(self):
        products = Product.objects.filter(category=self.kwargs['category_id'])

        product_ids = [product.id for product in products]
        features = Feature.objects.filter(product__id__in=product_ids)
        return features