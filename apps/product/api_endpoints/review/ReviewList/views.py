from rest_framework.generics import ListAPIView

from apps.product.models import Review

from .serializers import ReviewListSerializer


class ReviewListAPIView(ListAPIView):
    serializer_class = ReviewListSerializer

    def get_queryset(self):
        queryset = Review.objects.filter(user=self.request.user)
        return queryset