from django.urls import path  # noqa: F401

from apps.cart.api_endpoints.cart import CartDetailAPIView, CartItemListAPIView, CartItemCreateAPIView, \
    CartItemDeleteFromCartAPIView, ChangeCartItemQTYAPIView

urlpatterns = [
    path("detail/", CartDetailAPIView.as_view(), name='cart-detail'),
    path("cart-item/list/", CartItemListAPIView.as_view(), name='cart-item-list'),
    path("cart-item/create/", CartItemCreateAPIView.as_view(), name='cart-item-create'),
    path("cart-item/delete/<int:product_id>/", CartItemDeleteFromCartAPIView.as_view(),
         name='cart-item-delete-from-cart'),
    path("cart-item/change-qty/", ChangeCartItemQTYAPIView.as_view(), name='cart-item-change-qty'),
]
