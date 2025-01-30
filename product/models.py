from django.db import models



# Category model:
class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    image = models.ImageField(upload_to='categories/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name



# Product Model:
class Product(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/')
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    stock = models.IntegerField()
    rating = models.DecimalField(max_digits=3, decimal_places=2, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



# Testimonial model:
class Testimonial(models.Model):
    customer_name = models.CharField(max_length=255)
    review = models.TextField()
    rating = models.DecimalField(max_digits=3, decimal_places=2)
    product = models.ForeignKey(Product, related_name='testimonials', on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
