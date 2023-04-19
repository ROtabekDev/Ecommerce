from rest_framework.generics import CreateAPIView

from .serializers import ReviewCreateSerializer


class ReviewCreateAPIView(CreateAPIView):
    serializer_class = ReviewCreateSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)