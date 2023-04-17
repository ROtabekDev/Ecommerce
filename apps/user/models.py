from django.db import models
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager,
                                        PermissionsMixin)
from phonenumber_field.modelfields import PhoneNumberField
from rest_framework_simplejwt.tokens import RefreshToken

from apps.common.models import BaseModel


class CustomUserManager(BaseUserManager):

    def create_user(self, first_name, last_name, phone_number, password=None):
        user = self.model(phone_number=phone_number, first_name=first_name, last_name=last_name)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, first_name, last_name, phone_number, password=None):
        user = self.model(
            phone_number=phone_number, first_name=first_name, last_name=last_name, password=make_password(password)
        )
        user.is_superuser = True
        user.is_admin = True
        user.is_staff = True
        user.save()
        return user


class User(AbstractBaseUser, PermissionsMixin, BaseModel):
    first_name = models.CharField("First name", max_length=100)
    last_name = models.CharField("Last name", max_length=100)
    phone_number = PhoneNumberField("Phone number", max_length=32, unique=True)
    email = models.EmailField("Email", unique=True, blank=True, null=True)
    avatar = models.ImageField(
        "Image", upload_to="user/user/avatar/", default="user/user/avatar/default-user.png"
    )
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = "phone_number"
    REQUIRED_FIELDS = ["first_name", "last_name"]

    objects = CustomUserManager()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

    def tokens(self):
        refresh = RefreshToken.for_user(self)

        return {"refresh": str(refresh), "access": str(refresh.access_token)}


class Notification(BaseModel):
    user = models.ForeignKey("user.User", on_delete=models.CASCADE, verbose_name="User")
    text = models.TextField('Text')
    viewed = models.BooleanField("Viewed", default=False)

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "Notification"
        verbose_name_plural = "Notifications"


class Wishlist(BaseModel):
    user = models.ForeignKey("user.User", on_delete=models.CASCADE, verbose_name="User")
    product = models.ForeignKey("product.Product", on_delete=models.CASCADE, verbose_name="Product")

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "Wishlist"
        verbose_name_plural = "Wishlists"


class PurchasedProduct(BaseModel):
    user = models.ForeignKey("user.User", on_delete=models.CASCADE, verbose_name="User")
    product = models.ForeignKey("product.Product", on_delete=models.CASCADE, verbose_name="Product")
    qty = models.PositiveIntegerField('Quantity')

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "Purchased product"
        verbose_name_plural = "Purchased products"
