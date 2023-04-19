from modeltranslation.translator import register, TranslationOptions

from apps.common.models import Contact


@register(Contact)
class ContactTranslationOptions(TranslationOptions):
    fields = ('text',)
