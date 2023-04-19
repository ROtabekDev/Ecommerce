from django.urls import path  # noqa: F401

from apps.product.api_endpoints.Brand import BrandListAPIView
from apps.product.api_endpoints.Category import CategoryListAPIView

from apps.product.api_endpoints.review import ReviewCreateAPIView, ReviewDeleteAPIView, ReviewListAPIView

urlpatterns = [
    # Category
    path("category-list/", CategoryListAPIView.as_view(), name="category-list"),

    # Brand
    path("brand-list/", BrandListAPIView.as_view(), name="brand-list"),

    # review
    path('review/list/', ReviewListAPIView.as_view(), name='review-list'),
    path('review/create/', ReviewCreateAPIView.as_view(), name='review-create'),
    path('review/delete/<int:product_id>/', ReviewDeleteAPIView.as_view(), name='review-delete'),
]
