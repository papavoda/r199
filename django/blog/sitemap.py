from django.contrib.sitemaps import Sitemap
from .models import Post
from django.shortcuts import reverse


class PostSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.8
    protocol = 'https'

    def items(self):
        return Post.objects.filter(status='published')

    def lastmod(self, obj):
        return obj.pub_at


class StaticSitemap(Sitemap):
    priority = 0.8
    changefreq = 'daily'
    protocol = 'https'

    def items(self):
        return ['home', 'about', 'price', 'post_list', 'favorites_list', 'calc']

    def location(self, item):
        if item == 'calc':
            return '/calc/'  # SPA served separately by the production web server.
        return reverse(item)


class ServiceSitemap(Sitemap):
    protocol = 'https'
    changefreq = 'monthly'
    priority = 0.8

    def items(self):
        from .site_content import SERVICES
        return list(SERVICES)

    def location(self, item):
        return reverse('service_detail', kwargs={'service_slug': item})
