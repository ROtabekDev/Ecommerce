from django.urls import path  # noqa: F401

from apps.product.api_endpoints.review import ReviewCreateAPIView, ReviewDeleteAPIView, ReviewListAPIView

urlpatterns = [
    # review
    path('review/list/', ReviewListAPIView.as_view(), name='review-list'),
    path('review/create/', ReviewCreateAPIView.as_view(), name='review-create'),
    path('review/delete/<int:product_id>/', ReviewDeleteAPIView.as_view(), name='review-delete'),
]