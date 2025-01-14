from django.urls import path, include
from rest_framework import routers
from .views import FAQViewSet

router = routers.SimpleRouter()
router.register(r'faqs', FAQViewSet, basename='faq')



urlpatterns = [
    path('comments/', include(router.urls)),
]