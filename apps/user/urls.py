from django.urls import path  # noqa: F401

from apps.user.api_endpoints.user import UserRegisterAPIView, UserLoginAPIView

from apps.user.api_endpoints.wishlist import WishlistCreateAPIView, WishlistListAPIView, WishlistDeleteAPIView

urlpatterns = [
    path('register/', UserRegisterAPIView.as_view(), name='user-register'),
    path('login/', UserLoginAPIView.as_view(), name='user-login'),

    # wishlist
    path('wishlist/create/', WishlistCreateAPIView.as_view(), name='wishlist-create'),
    path('wishlist/list/', WishlistListAPIView.as_view(), name='wishlist-list'),
    path('wishlist/delete/<int:product_id>/', WishlistDeleteAPIView.as_view(), name='wishlist-delete'),
]
