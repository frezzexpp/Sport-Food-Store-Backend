from rest_framework import serializers
from .models import Category, Product, Testimonial


# Category Serializer:
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


# Product Serializer:
class ProductSerializers(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category.name', read_only=True)

    class Meta:
        model = Product
        fields = ['id', 'image', 'name', 'description', 'price', 'category_name']


#Project Details Serializer:
class ProductDetailsSerializers(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category.name', read_only=True)

    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'image', 'stock', 'rating', 'created_at', 'updated_at', 'category_name']



# Testimonial Serializer:
class TestimonialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testimonial
        fields = '__all__'