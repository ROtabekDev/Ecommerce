from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models  # noqa: F401

from apps.common.models import BaseModel

from .choices import CurrencyType


class Product(BaseModel):
    title = models.CharField("Title", max_length=150)
    slug = models.CharField("Slug", max_length=150)
    category = models.ForeignKey("product.Category", on_delete=models.CASCADE, verbose_name="Category")
    brand = models.ForeignKey("product.Brand", on_delete=models.CASCADE, verbose_name="Brand")
    price = models.DecimalField("Price", max_digits=10, decimal_places=2)
    is_discount = models.BooleanField("Is discount", default=False)
    discount_price = models.DecimalField("Discount price", max_digits=10, decimal_places=2, default=0)
    currency_type = models.CharField("Currency", max_length=10, choices=CurrencyType.choices, default=CurrencyType.UZS)
    qty = models.PositiveIntegerField("Quantity", default=0)
    available = models.BooleanField("Available", default=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"


class Category(BaseModel):
    parent = models.ForeignKey(
        "product.Category", on_delete=models.CASCADE, verbose_name="Parent", blank=True, null=True
    )
    title = models.CharField("Title", max_length=150)
    slug = models.CharField("Slug", max_length=150)
    logo = models.ImageField("Logo", upload_to="product/category/logo/")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"


class Brand(BaseModel):
    title = models.CharField("Title", max_length=150)
    slug = models.CharField("Slug", max_length=150)
    logo = models.ImageField("Logo", upload_to="product/brand/logo/")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Brand"
        verbose_name_plural = "Brands"


class Feature(BaseModel):
    product = models.ForeignKey("product.Product", on_delete=models.CASCADE, verbose_name="Product")
    feature_name = models.ForeignKey("product.FeatureName", on_delete=models.CASCADE, verbose_name="Feature name")
    value = models.CharField("Value", max_length=150)

    def __str__(self):
        return self.feature_name.title

    class Meta:
        verbose_name = "Feature"
        verbose_name_plural = "Features"


class FeatureName(BaseModel):
    title = models.CharField("Title", max_length=150)
    slug = models.CharField("Slug", max_length=150)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Feature name"
        verbose_name_plural = "Feature names"


class ProductImages(BaseModel):
    product = models.ForeignKey("product.Product", on_delete=models.CASCADE, verbose_name="Product")
    image = models.ImageField("Image", upload_to="product/product-images/image/")
    use_for_slider = models.BooleanField("Use for slider", default=False)

    def __str__(self):
        return f"For {self.product.title}"

    class Meta:
        verbose_name = "Product image"
        verbose_name_plural = "Product images"


class Review(BaseModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="User")
    product = models.ForeignKey("product.Product", on_delete=models.CASCADE, verbose_name="Product")
    rating_number = models.PositiveIntegerField(
        "Rating number ", validators=[MinValueValidator(0), MaxValueValidator(5)], default=0
    )
    text = models.CharField("Text", max_length=250)

    def __str__(self):
        return f"{self.rating_number} {self.text}"

    class Meta:
        verbose_name = "Review"
        verbose_name_plural = "Reviews"
        unique_together = ('user', 'product')