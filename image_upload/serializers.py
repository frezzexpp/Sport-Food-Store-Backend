from rest_framework import serializers
from .models import UploadImage



# UploadImage serializer:
class UploadImageSerializers(serializers.ModelSerializer):
    class Meta:
        model = UploadImage
        fields = "__all__"