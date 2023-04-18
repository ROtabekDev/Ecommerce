from django.contrib import admin  # noqa: F401

from .models import Cart, CartItem, CartProduct, Order, Region, District, PaymentType


@admin.register(CartItem)
class CartItemModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'cart', 'product', 'qty', 'final_price')
    list_display_links = ('id', 'cart', 'product')
    list_filter = ('cart',)


@admin.register(Cart)
class CartModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'total_products', 'final_price', 'in_order')
    list_display_links = ('id', 'user')
    list_filter = ('user',)


@admin.register(CartProduct)
class CartProductModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'cart', 'product')
    list_display_links = ('id', 'cart', 'product')
    list_filter = ('cart',)


@admin.register(Order)
class OrderModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'cart', 'first_name', 'last_name', 'phone_number')
    list_display_links = ('id', 'user', 'cart', 'first_name', 'last_name', 'phone_number')
    list_filter = ('user',)


@admin.register(Region)
class RegionModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    prepopulated_fields = {"slug": ("title",)}
    list_display_links = ('id', 'title',)


@admin.register(District)
class DistrictModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'region')
    prepopulated_fields = {"slug": ("title",)}
    list_display_links = ('id', 'title')
    list_filter = ('region',)


@admin.register(PaymentType)
class PaymentTypeModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    prepopulated_fields = {"slug": ("title",)}
    list_display_links = ('id', 'title')
