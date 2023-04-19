from django.urls import path  # noqa: F401

from apps.common.api_endpoints.contact import ContanctCreateAPIView

urlpatterns = [
    path('contact/create/', ContanctCreateAPIView.as_view(), name='contact-create')
]
