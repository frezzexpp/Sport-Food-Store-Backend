from django.shortcuts import render
from drf_spectacular.utils import extend_schema_view, extend_schema
from rest_framework import viewsets
from common.permissions import IsAdminOrReadOnly
from rest_framework.permissions import  IsAuthenticatedOrReadOnly
from .serializers import CategorySerializer, ProductSerializers, TestimonialSerializer, ProductDetailsSerializers
from .models import Category, Product, Testimonial



# CategoryViewSet:
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

# CategoryViewSet:
@extend_schema_view(
    list=extend_schema(summary='List Categories', tags=['Category']),
    retrieve=extend_schema(summary='Retrieve Category', tags=['Category']),
    create=extend_schema(summary='Create Category', tags=['Category']),
    update=extend_schema(summary='Update Category', tags=['Category']),
    partial_update=extend_schema(summary='Partial Update Category', tags=['Category']),
    destroy=extend_schema(summary='Delete Category', tags=['Category']),
)
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (IsAdminOrReadOnly, )

# ProductViewSet:
@extend_schema_view(
    list=extend_schema(summary='List Products', tags=['Product']),
    retrieve=extend_schema(summary='Retrieve Product', tags=['Product']),
    create=extend_schema(summary='Create Product', tags=['Product']),
    update=extend_schema(summary='Update Product', tags=['Product']),
    partial_update=extend_schema(summary='Partial Update Product', tags=['Product']),
    destroy=extend_schema(summary='Delete Product', tags=['Product']),
)
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers
    permission_classes = (IsAdminOrReadOnly, )

# ProductDetailsViewSet:
@extend_schema_view(
    list=extend_schema(summary='List Products', tags=['Product Details']),
    retrieve=extend_schema(summary='Retrieve Product', tags=['Product Details']),
    create=extend_schema(summary='Create Product', tags=['Product Details']),
    update=extend_schema(summary='Update Product', tags=['Product Details']),
    partial_update=extend_schema(summary='Partial Update Product', tags=['Product Details']),
    destroy=extend_schema(summary='Delete Product', tags=['Product Details']),
)
class ProductDetailsViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductDetailsSerializers
    permission_classes = (IsAdminOrReadOnly, )




# TestimonialViewSet:
@extend_schema_view(
    list=extend_schema(summary='List Testimonials', tags=['Testimonial']),
    retrieve=extend_schema(summary='Retrieve Testimonial', tags=['Testimonial']),
    create=extend_schema(summary='Create Testimonial', tags=['Testimonial']),
    update=extend_schema(summary='Update Testimonial', tags=['Testimonial']),
    partial_update=extend_schema(summary='Partial Update Testimonial', tags=['Testimonial']),
    destroy=extend_schema(summary='Delete Testimonial', tags=['Testimonial']),
)
class TestimonialViewSet(viewsets.ModelViewSet):
    queryset = Testimonial.objects.all()
    serializer_class = TestimonialSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )
