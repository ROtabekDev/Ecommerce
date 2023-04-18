from django.contrib import admin  # noqa: F401

from .models import User, Notification, Wishlist, PurchasedProduct


@admin.register(User)
class UserModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'phone_number')
    list_display_links = ('id', 'first_name', 'last_name', 'phone_number')


@admin.register(Notification)
class NotificationModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'text', 'viewed')
    list_display_links = ('id', 'user',)
    list_filter = ('user',)


@admin.register(Wishlist)
class WishlistModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'product')
    list_display_links = ('id', 'user',)
    list_filter = ('user',)


@admin.register(PurchasedProduct)
class PurchasedProductModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'product', 'qty')
    list_display_links = ('id', 'user',)
    list_filter = ('user',)
