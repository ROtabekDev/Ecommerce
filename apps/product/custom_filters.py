from django_filters import rest_framework as filters
from .models import Product


class ProductListFilter(filters.FilterSet):
    min_price = filters.NumberFilter(field_name="price", lookup_expr='gte')
    max_price = filters.NumberFilter(field_name="price", lookup_expr='lte')
    feature = filters.CharFilter(method='filter_by_feature_value')

    class Meta:
        model = Product
        fields = ['brand', 'min_price', 'max_price', 'feature']

    def filter_by_feature_value(self, queryset, name, data):
        data = data.split(':')
        title = data[0]
        value = data[1]
        return queryset.filter(feature__feature_name__title=title, feature__value=value)
