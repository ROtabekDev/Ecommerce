from rest_framework.serializers import ModelSerializer

from apps.common.models import Contact


class ContactCreateSerializer(ModelSerializer):

    class Meta:
        model = Contact
        fields = ('first_name', 'last_name', 'phone_number', 'text')