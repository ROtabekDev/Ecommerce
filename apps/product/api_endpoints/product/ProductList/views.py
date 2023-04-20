from rest_framework.generics import ListAPIView

from apps.product.models import Product

from .serializers import ProductListSerializer


class ProductListAPIView(ListAPIView):
    serializer_class = ProductListSerializer

    def get_queryset(self):
        queryset = Product.objects.filter(category=self.kwargs['category_id'])
        return queryset