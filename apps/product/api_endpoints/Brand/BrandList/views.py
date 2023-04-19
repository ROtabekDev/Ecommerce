from rest_framework.generics import ListAPIView

from apps.product.api_endpoints.Brand.BrandList.serializers import BrandListSerializer
from apps.product.models import Brand


class BrandListAPIView(ListAPIView):
    serializer_class = BrandListSerializer
    queryset = Brand.objects.all()


__all__ = ["BrandListAPIView"]
