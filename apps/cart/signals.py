from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete

from .models import CartItem


@receiver(post_save, sender=CartItem)
def create_cart_product(sender, instance, created, **kwargs):
    if created:
        CartProduct.objects.create(cart=instance.cart, product=instance)


@receiver(post_delete, sender=CartItem)
def delete_cart_product(sender, instance, **kwargs):
    cart_product = CartProduct.objects.get(cart=instance.cart, product=instance)
    cart_product.delete()