from django.db import models


class Category(models.Model):
    slug = models.SlugField()
    title = models.CharField(max_length=255)
    parent = models.ForeignKey(
        'Category', on_delete=models.CASCADE, related_name='children', blank=True, null=True)
    
class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='media/products/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')


class Product_Varient(models.Model):
    product_id = models.IntegerField()
    price = models.IntegerField()
    items_count = models.IntegerField()
    
    
