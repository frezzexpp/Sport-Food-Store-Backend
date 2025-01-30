from django.db import models



# UploadImage model:
class UploadImage(models.Model):
    image = models.ImageField(upload_to=" ")