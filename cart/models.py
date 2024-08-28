from django.db import models
from django.conf import settings

from store.models import Product_Variant


class Basket(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='basket')


class Basket_Item(models.Model):
    backet = models.ForeignKey(
        Basket, on_delete=models.CASCADE, related_name='basket_items')
    product = models.ForeignKey(
        Product_Variant, on_delete=models.CASCADE, related_name='basket_items')
    item_count = models.PositiveSmallIntegerField()
