from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import FAQ

@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ('question', 'created_at', 'updated_at')
    search_fields = ('question',)
    readonly_fields = ('created_at', 'updated_at')
