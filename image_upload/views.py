from drf_spectacular.utils import extend_schema_view, extend_schema
from rest_framework import mixins
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import GenericViewSet
from .serializers import *



# UploadImage view:
@extend_schema_view(
    create=extend_schema(summary='Upload', tags=['Upload-image'])
)

class UploadImageView(mixins.CreateModelMixin,
                   GenericViewSet):
    serializer_class = UploadImageSerializers
    queryset = UploadImage.objects.all()