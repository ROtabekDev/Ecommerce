from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny
from apps.product.models import Product
from apps.product.custom_filters import ProductListFilter

from .serializers import ProductListSerializer


class ProductListAPIView(ListAPIView):
    serializer_class = ProductListSerializer
    permission_classes = (AllowAny,)
    filterset_class = ProductListFilter

    def get_queryset(self):
        queryset = Product.objects.filter(category=self.kwargs['category_id'])
        return queryset
