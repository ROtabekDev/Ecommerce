from rest_framework.generics import ListAPIView
from django.db.models import Q
from apps.product.models import Product
from apps.user.models import PurchasedProduct

from .serializers import RelatedProductListSerializer


class RelatedProductListAPIView(ListAPIView):
    serializer_class = RelatedProductListSerializer

    def get_queryset(self):
        product = Product.objects.get(id=self.kwargs['product_id'])
        purchased_products = PurchasedProduct.objects.exclude(Q(product=product) | Q(user=self.request.user)).filter(
            product__category=product.category).order_by('-qty')[:5]

        product_ids = [purchased_product.product_id for purchased_product in purchased_products]
        products = Product.objects.filter(id__in=product_ids)
        return products
