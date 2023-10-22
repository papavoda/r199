from django.contrib import admin
from .models import Price, PriceCategory


# Register your models here.
@admin.register(Price)
class PriceAdmin(admin.ModelAdmin):
    class Meta:
        filtered = 'pk'

    list_per_page = 10
    list_display = ['pk', 'name', 'dimension', 'price', 'category']
    list_editable = ['price']

    # inlines = [ImageInline, ]
    # prepopulated_fields = {'num': ('pk',)}


@admin.register(PriceCategory)
class PriceCategoryAdmin(admin.ModelAdmin):
    class Meta:
        filtered = 'pk'

    list_display = ['pk', 'name', 'slug']

