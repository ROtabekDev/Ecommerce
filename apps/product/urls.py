from django.urls import path  # noqa: F401

from apps.product.api_endpoints.Brand import BrandListAPIView
from apps.product.api_endpoints.Category import CategoryListAPIView

from apps.product.api_endpoints.review import ReviewCreateAPIView, ReviewDeleteAPIView, ReviewListAPIView
from apps.product.api_endpoints.product import (
    ProductDetailAPIView, ProductListAPIView, GetProductFeaturesListAPIView,
    RelatedProductListAPIView
)
from apps.product.api_endpoints.feature import FeatureListByCategoryListAPIView

urlpatterns = [

    # product
    path('list/<int:category_id>/', ProductListAPIView.as_view(), name='product-list'),
    path('detail/<int:pk>/', ProductDetailAPIView.as_view(), name='product-detail'),
    path('get-product-features/<int:product_id>/', GetProductFeaturesListAPIView.as_view(),
         name='get-product-features'),

    path('related-product/list/<int:product_id>/', RelatedProductListAPIView.as_view(), name='related-product-list'),

    # feature
    path('features-by-category/list/<int:category_id>/', FeatureListByCategoryListAPIView.as_view(),
         name='features-by-category-list'),

    # Category
    path("category-list/", CategoryListAPIView.as_view(), name="category-list"),

    # Brand
    path("brand-list/", BrandListAPIView.as_view(), name="brand-list"),

    # review
    path('review/list/', ReviewListAPIView.as_view(), name='review-list'),
    path('review/create/', ReviewCreateAPIView.as_view(), name='review-create'),
    path('review/delete/<int:product_id>/', ReviewDeleteAPIView.as_view(), name='review-delete'),
]
