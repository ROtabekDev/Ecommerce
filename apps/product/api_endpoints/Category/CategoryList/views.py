from rest_framework.generics import ListAPIView

from apps.product.api_endpoints.Category.CategoryList.serializers import CategoryListSerializer
from apps.product.models import Category


class CategoryListAPIView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryListSerializer


__all__ = ["CategoryListAPIView"]
