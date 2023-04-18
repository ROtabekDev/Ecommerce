from django.http import Http404
from rest_framework.generics import DestroyAPIView
from rest_framework.response import Response

from apps.cart.models import CartItem, Cart, CartProduct
from apps.product.models import Product
from apps.cart.utils import update_cart


class CartItemDeleteFromCartAPIView(DestroyAPIView):
    queryset = CartItem.objects.all()

    def destroy(self, request, *args, **kwargs):

        try:
            product = Product.objects.get(id=self.kwargs['product_id'])
        except Product.DoesNotExist:
            raise Http404("Product not found")

        user = self.request.user

        cart = Cart.objects.filter(user=user, in_order=False).first()

        cart_item = CartItem.objects.get(
            cart=cart, product=product
        )

        cart_item.delete()

        update_cart(cart=cart)

        return Response({"status": 204, "message": "Product removed to cart."})
