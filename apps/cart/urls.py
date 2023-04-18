from django.urls import path  # noqa: F401

from apps.cart.api_endpoints.cart import CartDetailAPIView, CartItemListAPIView

urlpatterns = [
    path("detail/", CartDetailAPIView.as_view(), name='cart-detail'),
    path("cart-item/list/", CartItemListAPIView.as_view(), name='cart-item-list'),
]
