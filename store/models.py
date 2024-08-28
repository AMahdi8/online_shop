from django.db import models
from django.core.exceptions import ValidationError
from django.template.defaultfilters import slugify


class Category(models.Model):
    slug = models.SlugField()
    title = models.CharField(max_length=255)
    parent = models.ForeignKey(
        'Category', on_delete=models.CASCADE, related_name='children', blank=True, null=True)
    product_attributes_schema = models.JSONField(
        default=dict, blank=True, null=True)
    variant_attributes_schema = models.JSONField(
        default=dict, blank=True, null=True)

    def __str__(self) -> str:
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super(Category, self).save(*args, **kwargs)

    @property
    def is_leaf(self):
        return self.children.count() == 0


class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name='products')
    attributes = models.JSONField(blank=True, null=True)

    def __str__(self) -> str:
        return self.title

    def clean(self):
        if not self.category.is_leaf():
            raise ValidationError("The category must be a leaf category.")


class Product_Variant(models.Model):
    product_id = models.IntegerField()
    price = models.IntegerField()
    items_count = models.IntegerField()
    attributes = models.JSONField(default=dict, blank=True, null=True)

    def __str__(self):
        return f"{self.product.title} Variant"


class Product_Image(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='media/products/')
