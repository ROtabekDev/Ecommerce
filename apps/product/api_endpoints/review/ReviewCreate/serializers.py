from rest_framework.serializers import ModelSerializer

from apps.product.models import Review


class ReviewCreateSerializer(ModelSerializer):
    class Meta:
        model = Review
        fields = ('product', 'rating_number', 'text')
        read_only_fields = ('user',)

    def create(self, validated_data):
        user = self.context["request"].user

        try:
            review = Review.objects.get(product=validated_data["product"], user=user)
            review.delete()
            review = Review.objects.create(user=user,
                                           product=validated_data["product"],
                                           rating_number=validated_data["rating_number"],
                                           text=validated_data["text"])
        except Review.DoesNotExist:
            review = Review.objects.create(user=user,
                                           product=validated_data["product"],
                                           rating_number=validated_data["rating_number"],
                                           text=validated_data["text"])

        return review
