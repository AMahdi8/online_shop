# Generated by Django 5.0.7 on 2024-08-28 14:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0001_initial'),
        ('store', '0005_remove_product_image_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basket_item',
            name='backet',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='basket_items', to='cart.basket'),
        ),
        migrations.AlterField(
            model_name='basket_item',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='basket_items', to='store.product_variant'),
        ),
    ]
