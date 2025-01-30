from django.urls import path, include
from rest_framework import routers
from .views import UploadImageView

router = routers.SimpleRouter()
router.register(r'uploads', UploadImageView, basename='upload')



urlpatterns = [
    path('upload-images/', include(router.urls)),
]