from django.urls import path, include
from rest_framework import routers

from product.views import *

router = routers.SimpleRouter()
router.register(r'categories', CategoryViewSet, basename='category')
router.register(r'products', ProductViewSet, basename='product')
router.register(r'productdetails', ProductDetailsViewSet, basename='productdetail')
router.register(r'testimonials', TestimonialViewSet, basename='testimonial')


urlpatterns = [
    path('product/', include(router.urls)),
]