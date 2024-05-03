from django.db import models
# для организации вложенности
from mptt.models import MPTTModel, TreeForeignKey
from django.utils import timezone
from django.contrib.auth.models import User
from django.shortcuts import reverse
from autoslug import AutoSlugField
from django.template.defaultfilters import slugify  # new
from django_ckeditor_5.fields import CKEditor5Field

class Category(MPTTModel):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, null=False, unique=True)
    parent = TreeForeignKey(
        'self',
        related_name="children",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )

    # def get_absolute_url(self):
    #     return reverse("category_detail", kwargs={'app_name': self.app_name, 'cat_slug': self.category.slug, 'pk': self.pk})

    def __str__(self):
        return self.name

    class MPTTMeta:
        order_insertion_by = ['name']

    def save(self, *args, **kwargs):  # new
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)

    def get_absolute_url(self):
        # '<slug:slug>/<slug:post_slug>'
        return reverse("category_detail", kwargs={'pk': self.pk})


class Tag(models.Model):
    name = models.CharField(max_length=50)
    slug = AutoSlugField(populate_from='name', unique=True)

    def get_absolute_url(self):
        return reverse('tag_detail', kwargs={'slug': self.slug})

    def __str__(self):
        return self.name


def upload_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return f'articles/{instance.author}/{instance.slug}/{filename}'


class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    keywords = models.CharField(max_length=100, default='')
    description = models.CharField(max_length=500, default='')
    title = models.CharField(max_length=500)
    # slug = models.SlugField(max_length=64, null=True, blank=True)
    # TODO check autoslug
    slug = AutoSlugField(populate_from='title', unique=True)
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name='blog_posts')
    main_image = models.ImageField(verbose_name='Изображение', upload_to=upload_directory_path, blank=True, null=True)
    # image = models.ImageField(upload_to='articles/%Y/%m/%d/%pk', null=True, blank=True)

    intro = models.TextField(max_length=500, default='',
                             help_text='Little intro text')
    # RichTextField -> for ckeditor
    text = CKEditor5Field(max_length=8000, verbose_name='Основной текст', config_name='extends')

    category = models.ForeignKey(Category, related_name="post",
                                 on_delete=models.SET_NULL,
                                 null=True,
                                 )
    tags = models.ManyToManyField(Tag, verbose_name='Метки', related_name="post")
    pub_at = models.DateTimeField(auto_now_add=True)
    changed = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10,
                              choices=STATUS_CHOICES,
                              default='draft')
    is_favorite = models.BooleanField(default=False, help_text='В избранное', )
    views_count = models.BigIntegerField(default=0, null=True, blank=True, verbose_name='Количество просмотров', )

    class Meta:
        ordering = ('-pub_at',)

    app_name = __package__

    def get_absolute_url(self):
        return reverse("post_detail",
                       kwargs={'app_name': self.app_name, 'cat_slug': self.category.slug, 'slug': self.slug})

    def get_tags(self):
        return self.tags.all()

    def get_comments(self):
        return self.comment.all().filter(active=True)

    def get_images(self):
        return self.images.all()

    def get_youtube(self):
        return self.youtube.all()

    def save(self, *args, **kwargs):  # new
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.category} - {self.title}'


# https://youtu.be/EWmsWPaM-Oc?t=266
class Comment(models.Model):
    post = models.ForeignKey(Post, related_name="comment", on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    # website = models.URLField(max_length=200, null=True, blank=True)
    message = models.TextField(max_length=500)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=False)
    # default_avatar = models.ImageField(default='')

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return 'Comment by {} on {}'.format(self.name, self.post)


class Favorites(models.Model):
    is_favorites = False


# for Image upload
def image_upload_directory(instance, filename):
    # file will be uploaded to MEDIA_ROOT/instance.post.author/instance.post.slug/<filename>
    return f'articles/{instance.post.author}/{instance.post.slug}/{filename}'


class Image(models.Model):
    name = models.CharField(max_length=50, default='')  # alt
    post = models.ForeignKey(Post, related_name='images', on_delete=models.SET_NULL, null=True)
    image = models.ImageField(upload_to=image_upload_directory)

    def __str__(self):
        return f'{self.name} - {self.image}'


class VideoYoutube(models.Model):
    name = models.CharField(max_length=250, default='', blank=True, null=True)
    post = models.ForeignKey(Post, related_name='youtube', on_delete=models.SET_NULL, null=True)
    video_frame = models.TextField(max_length=900)

    def __str__(self):
        if self.name:
            return self.name



class Menu(models.Model):
    title = models.CharField(max_length=16)
    url = models.URLField(max_length=200)
    visible = models.BooleanField(default=True)
