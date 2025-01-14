from rest_framework import serializers
from .models import FAQ

# FAQ serializer:
class FAQSerializer(serializers.ModelSerializer):
    class Meta:
        model = FAQ
        fields = ['id', 'question', 'answer', 'created_at', 'updated_at']
