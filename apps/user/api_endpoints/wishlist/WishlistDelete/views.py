from django.http import Http404
from rest_framework.generics import DestroyAPIView
from rest_framework.response import Response

from django.core.exceptions import ObjectDoesNotExist
from apps.user.models import Wishlist


class WishlistDeleteAPIView(DestroyAPIView):
    queryset = Wishlist.objects.all()

    def destroy(self, request, *args, **kwargs):
        try:
            product = Wishlist.objects.get(user=self.request.user, product=self.kwargs['product_id'])
            product.delete()
            return Response({"status": 204, "message": "Product removed to wishlist."})
        except ObjectDoesNotExist:
            raise Http404("Product not found")
