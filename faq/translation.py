from modeltranslation.decorators import register
from modeltranslation.translator import TranslationOptions
from .models import FAQ



# Faq translation:
@register(FAQ)
class FAQTranslationOptions(TranslationOptions):
    fields = ('question', 'answer')