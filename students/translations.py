from modeltranslation.translator import register, TranslationOptions

from .models import Region


@register(Region)
class RegionTranslationOptions(TranslationOptions):
    fields = ('name',)
