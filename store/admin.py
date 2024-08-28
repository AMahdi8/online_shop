from django.contrib import admin
from django import forms

from .models import Category, Product, Product_Variant


class JSONSchemaTextarea(forms.Textarea):
    def __init__(self, attrs=None):
        final_attrs = {'cols': '80', 'rows': '20'}
        if attrs is not None:
            final_attrs.update(attrs)
        super().__init__(final_attrs)


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['title', 'slug', 'parent',
                  'product_attributes_schema', 'variant_attributes_schema']
        widgets = {
            'product_attributes_schema': JSONSchemaTextarea(),
            'variant_attributes_schema': JSONSchemaTextarea(),
        }


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    form = CategoryForm
    list_display = ['title', 'parent', 'slug']
    search_fields = ['title', 'slug']
    list_filter = ['parent']
    prepopulated_fields = {'slug': ['title']}
