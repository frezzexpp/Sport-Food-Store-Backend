from django.contrib import admin
from .models import Category, Product, Testimonial



# Category admin register:
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'updated_at')
    search_fields = ('name', 'description')
    list_filter = ('created_at',)
    readonly_fields = ('created_at', 'updated_at')



# Product admin register:
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category', 'stock', 'created_at')
    search_fields = ('name', 'description')
    list_filter = ('category', 'created_at')
    readonly_fields = ('created_at', 'updated_at')



# Testimonial admin register:
@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('customer_name', 'rating', 'product', 'created_at')
    search_fields = ('customer_name', 'review')
    list_filter = ('rating', 'created_at')
    readonly_fields = ('created_at', 'updated_at')
