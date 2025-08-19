from django.contrib import admin
from .models import Price, PriceCategory


# # Register your models here.
# @admin.register(Price)
# class PriceAdmin(admin.ModelAdmin):
#     class Meta:
#         filtered = 'pk'

#     list_per_page = 30
#     list_display = ['pk', 'name', 'dimension', 'price', 'category', 'use_in_calc']
#     list_editable = ['use_in_calc', ]

#     # inlines = [ImageInline, ]
#     # prepopulated_fields = {'num': ('pk',)}

from django.contrib import admin

@admin.register(Price)
class PriceAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'position', 'price', 'use_in_calc']
    list_editable = ['position', 'use_in_calc']
    list_filter = ['category', 'use_in_calc']
    ordering = ['category', 'position']
    actions = ['renumber_positions']
    
    def save_model(self, request, obj, form, change):
        if not change:  # Только при создании
            if obj.position == 0.0:
                obj.position = obj.get_next_position()
        super().save_model(request, obj, form, change)
    
    def renumber_positions(self, request, queryset):
        """Действие для перенумерации позиций в выбранной категории"""
        category = queryset.first().category
        items = Price.objects.filter(category=category).order_by('position')
        for i, item in enumerate(items, start=1):
            item.position = float(i)
            item.save()
        self.message_user(request, f"Позиции в категории {category} перенумерованы")
    renumber_positions.short_description = "Перенумеровать позиции"


@admin.register(PriceCategory)
class PriceCategoryAdmin(admin.ModelAdmin):
    class Meta:
        filtered = 'pk'

    list_display = ['pk', 'name', 'slug']

