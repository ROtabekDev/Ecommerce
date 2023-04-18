from django.contrib import admin  # noqa: F401

from .models import Product, Category, Brand, Feature, FeatureName, ProductImages, Review


@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'brand', 'price', 'available')
    prepopulated_fields = {"slug": ("title",)}
    list_display_links = ('id', 'title')
    list_filter = ('category', 'brand')


@admin.register(Category)
class CategoryModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    prepopulated_fields = {"slug": ("title",)}
    list_display_links = ('id', 'title',)


@admin.register(Brand)
class BrandModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    prepopulated_fields = {"slug": ("title",)}
    list_display_links = ('id', 'title',)


@admin.register(Feature)
class FeatureModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'feature_name', 'value')
    list_display_links = ('id', 'product', 'feature_name')
    list_filter = ('product',)


@admin.register(FeatureName)
class FeatureNameModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    prepopulated_fields = {"slug": ("title",)}
    list_display_links = ('id', 'title',)


@admin.register(ProductImages)
class ProductImagesModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'use_for_slider')
    list_display_links = ('id', 'product')
    list_filter = ('product',)


@admin.register(Review)
class ReviewModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'product', 'rating_number')
    list_display_links = ('id', 'user', 'product')
    list_filter = ('user', 'product')
