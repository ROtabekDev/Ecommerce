from modeltranslation.translator import register, TranslationOptions

from apps.user.models import Notification


@register(Notification)
class NotificationTranslationOptions(TranslationOptions):
    fields = ('text',)
