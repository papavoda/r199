"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import django.views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.contrib.sitemaps.views import sitemap

from blog.sitemap import PostSitemap, StaticSitemap
sitemaps = {
    'posts': PostSitemap,
    'static': StaticSitemap,
    }


urlpatterns = [
    path('admin/', admin.site.urls),
    path('ckeditor5/', include('django_ckeditor_5.urls')),
    path('', include('blog.urls')),
    path('', include('contact.urls')),
    path('', include('price.urls')),
    # path('', include('calc.urls')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path('api/v1/', include('api.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# FOR debug_toolbar
if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
                      path('__debug__/', include(debug_toolbar.urls)),
                  ] + urlpatterns

# handler404 = 'mysite.views.my_custom_page_not_found_view'
