from django.urls import path  # noqa: F401

from apps.product.api_endpoints.review import ReviewCreateAPIView, ReviewDeleteAPIView, ReviewListAPIView
from apps.product.api_endpoints.product import ProductDetailAPIView, GetProductFeaturesListAPIView

urlpatterns = [
    # product
    path('detail/<int:pk>/', ProductDetailAPIView.as_view(), name='product-detail'),
    path('get-product-features/<int:product_id>/', GetProductFeaturesListAPIView.as_view(), name='get-product-features'),

    # review
    path('review/list/', ReviewListAPIView.as_view(), name='review-list'),
    path('review/create/', ReviewCreateAPIView.as_view(), name='review-create'),
    path('review/delete/<int:product_id>/', ReviewDeleteAPIView.as_view(), name='review-delete'),
]