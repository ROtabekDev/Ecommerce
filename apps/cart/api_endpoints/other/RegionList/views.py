from rest_framework.generics import ListAPIView

from apps.cart.models import Region
from .serializers import RegionListSerializer


class RegionListAPIView(ListAPIView):
    queryset = Region.objects.all()
    serializer_class = RegionListSerializer
