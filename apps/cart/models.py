from django.conf import settings
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

from apps.common.models import BaseModel

from .choices import BuyigType, OrderStatus


class CartItem(BaseModel):
    cart = models.ForeignKey("cart.Cart", verbose_name="Cart", on_delete=models.CASCADE)
    product = models.ForeignKey("product.Product", on_delete=models.CASCADE, verbose_name="Product")
    qty = models.PositiveIntegerField("Quantity", default=1)
    final_price = models.DecimalField("Final price", max_digits=12, decimal_places=2, default=0)

    def save(self, *args, **kwargs):
        if self.product.is_discount:
            self.final_price = self.qty * self.product.discount_price
        else:
            self.final_price = self.qty * self.product.price
        super().save(*args, **kwargs)

    def __str__(self):
        return self.product.title

    class Meta:
        verbose_name = "Cart item"
        verbose_name_plural = "Cart items"


class Cart(BaseModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="User")
    total_products = models.IntegerField("Total products", default=0)
    final_price = models.DecimalField("Final price", max_digits=12, decimal_places=2, default=0)
    discount_price = models.DecimalField("Discount price", max_digits=12, decimal_places=2, default=0)
    discount_percentage = models.PositiveIntegerField("Discount percentage", default=0)
    shipping_cost = models.DecimalField(
        max_digits=12, decimal_places=2, verbose_name="Shipping cost", default=0
    )
    in_order = models.BooleanField("In order", default=False)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"

    class Meta:
        verbose_name = "Cart"
        verbose_name_plural = "Carts"


class CartProduct(BaseModel):
    cart = models.ForeignKey("cart.Cart", on_delete=models.CASCADE, verbose_name="Cart")
    product = models.ForeignKey("cart.CartItem", on_delete=models.CASCADE, verbose_name="Product")

    def __str__(self):
        return f"{self.cart.user.first_name} {self.cart.user.last_name}"

    class Meta:
        verbose_name = "Cart product"
        verbose_name_plural = "Cart products"


class Order(BaseModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="User")
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, verbose_name="Cart")
    first_name = models.CharField("First name", max_length=150)
    last_name = models.CharField("Last name", max_length=150)
    phone_number = PhoneNumberField("Phone number", max_length=32)
    buying_type = models.CharField("Buying type", choices=BuyigType.choices, max_length=20)
    region = models.ForeignKey("cart.Region", on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Region")
    district = models.ForeignKey(
        "cart.District", on_delete=models.SET_NULL, null=True, blank=True, verbose_name="District"
    )
    home_address = models.CharField("Home address", max_length=250)
    payment_type = models.ForeignKey(
        "cart.PaymentType", on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Payment type"
    )
    status = models.CharField("Status", choices=OrderStatus.choices, max_length=20, default="In_progress")

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.phone_number}"

    class Meta:
        verbose_name = "Order"
        verbose_name_plural = "Orders"


class Region(BaseModel):
    title = models.CharField("Title", max_length=50)
    slug = models.SlugField("Slug", max_length=50)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Region"
        verbose_name_plural = "Regions"


class District(BaseModel):
    title = models.CharField("Title", max_length=50)
    slug = models.SlugField("Slug", max_length=50)
    region = models.ForeignKey("cart.Region", on_delete=models.CASCADE, verbose_name="Region")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "District"
        verbose_name_plural = "Districts"


class PaymentType(BaseModel):
    title = models.CharField("Title", max_length=50)
    slug = models.SlugField("Slug", max_length=50)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Payment type"
        verbose_name_plural = "Payment types"
