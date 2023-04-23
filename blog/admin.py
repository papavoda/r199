from django.contrib import admin
from django.utils.safestring import mark_safe
# from . import models
from .models import *
from mptt.admin import MPTTModelAdmin

admin.site.register(
    Category,
    MPTTModelAdmin,
    list_display=(
        'pk',
        'slug',
        'name',
        'parent',

        # ...more fields if you feel like it...
    ),
    list_editable=['slug'],
    list_display_links=(
        'name',
    ),
    prepopulated_fields={'slug': ('name',)}  # new
)

admin.site.register(Tag)


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ("name", "image", 'get_image')

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="110" height="80"')

    get_image.short_description = "Миниатюра"


class ImageInline(admin.StackedInline):
    model = Image
    max_num = 20
    extra = 0
    list_display = ("name", "image", 'get_image')
    readonly_fields = ("get_image",)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="110" height="80"')


@admin.register(VideoYoutube)
class VideoYoutubeAdmin(admin.ModelAdmin):
    list_display = ("name", "video_frame")


class VideoYoutubeInline(admin.StackedInline):
    model = VideoYoutube
    max_num = 4
    extra = 0
    list_display = ("name", "video_frame",)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_per_page = 10
    list_display = ['pub_at', 'title', 'slug', 'get_image', 'author', 'status', 'is_favorite']
    list_editable = ['status', 'is_favorite']
    readonly_fields = ("get_image",)
    inlines = [ImageInline, VideoYoutubeInline, ]

    # prepopulated_fields = {'slug': ('title',)}  # new

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.main_image.url} width="110" height="80"')


class CommentAdmin(admin.ModelAdmin):
    list_editable = ['active']
    list_display = ['name', 'email', 'post', 'created', 'active']
    list_filter = ['active', 'created', 'updated']
    search_fields = ['name', 'email', 'body']


admin.site.register(Comment, CommentAdmin)
