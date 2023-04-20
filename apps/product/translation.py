from modeltranslation.translator import register, TranslationOptions

from apps.product.models import Product, Category, Feature, FeatureName, Review


@register(Product)
class ProductTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(Feature)
class FeatureTranslationOptions(TranslationOptions):
    fields = ('value',)


@register(FeatureName)
class FeatureNameTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(Review)
class ReviewTranslationOptions(TranslationOptions):
    fields = ('text',)
