from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny
from .serializers import BrandListByCategorySerializer
from apps.product.models import Brand, Product


class BrandListByCategoryListAPIView(ListAPIView):
    serializer_class = BrandListByCategorySerializer
    permission_classes = (AllowAny,)

    def get_queryset(self):
        products = Product.objects.filter(category=self.kwargs['category_id'])

        brand_ids = [product.brand.id for product in products]
        brands = Brand.objects.filter(id__in=brand_ids)
        return brands