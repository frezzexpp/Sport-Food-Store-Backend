from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from faq.models import FAQ
from faq.serializers import FAQSerializer
from common.permissions import IsAdminOrAuthenticatedOrReadOnly



# FAQViewSet:
@extend_schema_view(
    list=extend_schema(summary='List FAQs', tags=['FAQ']),
    retrieve=extend_schema(summary='Retrieve FAQ', tags=['FAQ']),
    create=extend_schema(summary='Create FAQ', tags=['FAQ']),
    update=extend_schema(summary='Update FAQ', tags=['FAQ']),
    partial_update=extend_schema(summary='Partial Update FAQ', tags=['FAQ']),
    destroy=extend_schema(summary='Delete FAQ', tags=['FAQ']),
)
class FAQViewSet(viewsets.ModelViewSet):
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)