from django.urls import path, include
from api.spectacular.urls import urlpatterns as doc_urls
from faq.urls import urlpatterns as faq_urls
from product.urls import urlpatterns as product_urls

app_name = 'api'

urlpatterns = [
]

urlpatterns += doc_urls
urlpatterns += product_urls
urlpatterns += faq_urls
