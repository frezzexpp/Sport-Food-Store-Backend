from modeltranslation.translator import  TranslationOptions
from modeltranslation.decorators import register
from .models import Category, Product, Testimonial



# Category translation:
@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name', 'description')



# Product translation:
@register(Product)
class ProductTranslationOptions(TranslationOptions):
    fields = ('name', 'description')



# Testimonial translation:
@register(Testimonial)
class TestimonialTranslationOptions(TranslationOptions):
    fields = ('customer_name', 'review')
