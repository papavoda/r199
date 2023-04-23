from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(ContactModel)
class ContactModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'create_at']
    list_display_links = ('name', )


class ImageAboutInLine(admin.StackedInline):
    model = ImageAbout
    # extra = 1 # количество рецептов
    max_num = 6


class PromoAboutInLine(admin.StackedInline):
    model = PromoAbout
    # extra = 3  # количество рецептов
    max_num = 3


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    # list_display = ['id', 'name', 'email', 'create_at']
    # list_display_links = ('name', )
    inlines = [PromoAboutInLine, ImageAboutInLine, ]


@admin.register(HomeHeroSlogans)
class HomeHeroSlogansAdmin(admin.ModelAdmin):
    list_display = ['id', 'hero_section', 'title', ]


@admin.register(PromoAbout)
class PromoAboutAdmin(admin.ModelAdmin):
    pass
    # list_display = ['id', 'name', 'email', 'create_at']
    # list_display_links = ('name', )


@admin.register(ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    pass


admin.site.register(ContactLink)
admin.site.register(Social)
