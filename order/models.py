from django.db import models
from django.conf import settings

from store.models import Product_Variant


class Order(models.Model):
    STATUS_CHOICES = (
        ('P', 'pending'),
        ('C', 'completed'),
        ('F', 'failed'),
    )

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='orders')
    address = models.CharField(max_length=255)
    price = models.IntegerField()
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='P')


class Order_item(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_items')
    product = models.ForeignKey(Product_Variant, on_delete=models.CASCADE, related_name='order_items')
    item_count = models.PositiveSmallIntegerField()
    price = models.IntegerField()

    
