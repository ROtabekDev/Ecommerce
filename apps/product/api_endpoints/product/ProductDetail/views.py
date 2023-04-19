from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import AllowAny

from .serializers import ProductDetailSerializer

from apps.product.models import Product


class ProductDetailAPIView(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer
    permission_classes = (AllowAny,)