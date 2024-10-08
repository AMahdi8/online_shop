# Generated by Django 5.0.7 on 2024-08-02 22:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_product_variant_delete_product_varient_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='product_attributes_schema',
            field=models.JSONField(blank=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='variant_attributes_schema',
            field=models.JSONField(blank=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='attributes',
            field=models.JSONField(blank=True),
        ),
        migrations.AlterField(
            model_name='product_variant',
            name='attributes',
            field=models.JSONField(blank=True),
        ),
    ]
