from typing import List, Union

from django.urls import URLPattern, URLResolver, path  # noqa: F401

urlpatterns: List[Union[URLPattern, URLResolver]] = []
