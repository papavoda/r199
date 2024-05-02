from django.contrib import admin
from .models import Price, PriceCategory


# Register your models here.
@admin.register(Price)
class PriceAdmin(admin.ModelAdmin):
    class Meta:
        filtered = 'pk'

    list_per_page = 30
    list_display = ['pk', 'name', 'dimension', 'price', 'category', 'use_in_calc']
    list_editable = ['use_in_calc', ]

    # inlines = [ImageInline, ]
    # prepopulated_fields = {'num': ('pk',)}


@admin.register(PriceCategory)
class PriceCategoryAdmin(admin.ModelAdmin):
    class Meta:
        filtered = 'pk'

    list_display = ['pk', 'name', 'slug']

