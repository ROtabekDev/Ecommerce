from django.urls import path  # noqa: F401

from apps.product.api_endpoints.Brand import BrandListAPIView
from apps.product.api_endpoints.Category import CategoryListAPIView

urlpatterns = [
    # Category
    path("category-list/", CategoryListAPIView.as_view(), name="category-list"),

    # Brand
    path("brand-list/", BrandListAPIView.as_view(), name="brand-list"),

]
