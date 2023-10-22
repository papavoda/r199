from django.contrib.sitemaps import Sitemap
from .models import Post
from django.shortcuts import reverse


class PostSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.8
    protocol = 'https'

    def items(self):
        return Post.objects.all()

    def lastmod(self, obj):
        return obj.pub_at


class StaticSitemap(Sitemap):
    priority = 0.8
    changefreq = 'daily'
    protocol = 'https'

    def items(self):
        return ['post_list', 'favorites_list']

    def location(self, item):
        return reverse(item)
