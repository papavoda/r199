from django.conf import settings
from django.http import HttpResponse
from django.template.loader import render_to_string


def robots_txt(request):
    # No request context: robots must not load contacts or depend on site data.
    content = render_to_string('robots.txt', {
        'sitemap_url': settings.SITE_PUBLIC_URL.rstrip('/') + '/sitemap.xml',
    })
    return HttpResponse(content, content_type='text/plain; charset=utf-8')
