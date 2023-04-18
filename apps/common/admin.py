from django.contrib import admin  # noqa: F401

from .models import Contact


@admin.register(Contact)
class ContactModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'phone_number', 'text')
    list_display_links = ('id', 'first_name', 'phone_number')
    list_filter = ('phone_number',)
