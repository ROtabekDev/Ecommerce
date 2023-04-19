from modeltranslation.translator import register, TranslationOptions

from apps.cart.models import Order


@register(Order)
class OrderTranslationOptions(TranslationOptions):
    fields = ('status',)
