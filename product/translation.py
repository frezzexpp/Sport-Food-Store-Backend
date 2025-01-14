from modeltranslation.translator import  TranslationOptions
from modeltranslation.decorators import register
from .models import Category, Product, Testimonial


@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name', 'description')


@register(Product)
class ProductTranslationOptions(TranslationOptions):
    fields = ('name', 'description')


@register(Testimonial)
class TestimonialTranslationOptions(TranslationOptions):
    fields = ('customer_name', 'review')
