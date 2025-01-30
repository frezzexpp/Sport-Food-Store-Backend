from django.urls import path, include
from api.spectacular.urls import urlpatterns as doc_urls
from faq.urls import urlpatterns as faq_urls
from product.urls import urlpatterns as product_urls
from users.urls import urlpatterns as users_urls
from image_upload.urls import urlpatterns as upload_urls

app_name = 'api'

urlpatterns = [
]

urlpatterns += users_urls
urlpatterns += product_urls
urlpatterns += upload_urls
urlpatterns += faq_urls
urlpatterns += doc_urls
