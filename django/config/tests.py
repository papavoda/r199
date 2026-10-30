from pathlib import Path
from urllib.robotparser import RobotFileParser

from django.conf import settings
from django.test import SimpleTestCase, RequestFactory, override_settings

from .views import robots_txt


class RobotsTests(SimpleTestCase):
    def test_public_pages_and_assets_are_allowed(self):
        response = robots_txt(RequestFactory().get('/robots.txt'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response['Content-Type'].startswith('text/plain'))
        parser = RobotFileParser()
        parser.parse(response.content.decode().splitlines())
        for path in ['/', '/about/', '/price/', '/favorites/', '/blog/', '/calc/',
                     '/uslugi/otdelka-kvartir/', '/search/?q=remont',
                     '/static/css/nstyle.css', '/static/js/site-ui.js', '/media/photo.webp']:
            with self.subTest(path=path):
                self.assertTrue(parser.can_fetch('Googlebot', 'https://remont199.com' + path))
        for path in ['/admin/', '/accounts/login/', '/api/v1/prices/', '/__debug__/',
                     '/ckeditor5/', '/contact_us/', '/comment/1/', '/blog/post-create/', '/index.php']:
            with self.subTest(path=path):
                self.assertFalse(parser.can_fetch('Googlebot', 'https://remont199.com' + path))

    @override_settings(SITE_PUBLIC_URL='https://remont199.com')
    def test_static_copy_matches_django_response(self):
        response = robots_txt(RequestFactory().get('/robots.txt'))
        static = (Path(settings.BASE_DIR) / 'static/robots.txt').read_text(encoding='utf-8')
        self.assertEqual(response.content.decode().strip(), static.strip())

    @override_settings(SITE_PUBLIC_URL='https://example.test/')
    def test_sitemap_uses_public_origin(self):
        response = robots_txt(RequestFactory().get('/robots.txt'))
        self.assertIn('Sitemap: https://example.test/sitemap.xml', response.content.decode())
