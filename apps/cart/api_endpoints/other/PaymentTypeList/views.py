from rest_framework.generics import ListAPIView

from apps.cart.models import PaymentType
from .serializers import PaymentTypeListSerializer


class PaymentTypeListAPIView(ListAPIView):
    queryset = PaymentType.objects.all()
    serializer_class = PaymentTypeListSerializer