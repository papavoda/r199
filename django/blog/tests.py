from django.contrib.admin.sites import site
from django.contrib.auth import get_user_model
from django.core.cache import cache
from django.test import TestCase

from contact.models import About, HomeHeroSlogans
from .models import Category, Comment, Image, Post, Tag
from .site_content import SERVICES
from price.models import Price, PriceCategory
from contact.models import ContactLink
import json
import re


class PublicPostTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.author = get_user_model().objects.create_user(username='author')
        cls.category = Category.objects.create(name='Repairs', slug='repairs')
        cls.tag = Tag.objects.create(name='Repair tag')
        cls.public = Post.objects.create(
            title='Published repair', author=cls.author, category=cls.category,
            status='published', text='Public article',
        )
        cls.draft = Post.objects.create(
            title='Unpublished secret repair', author=cls.author, category=cls.category,
            status='draft', text='Private article',
        )
        cls.public.tags.add(cls.tag)
        cls.draft.tags.add(cls.tag)
        About.objects.create(name='About', slogan='Repairs', text='About repairs')
        HomeHeroSlogans.objects.create(hero_section=1, small_title='Repairs', title='Home repairs')

    def setUp(self):
        cache.clear()

    def test_draft_detail_is_not_public(self):
        self.assertEqual(self.client.get(self.draft.get_absolute_url()).status_code, 404)
        self.client.force_login(self.author)
        self.assertEqual(self.client.get(self.draft.get_absolute_url()).status_code, 404)
        self.draft.refresh_from_db()
        self.assertEqual(self.draft.views_count, 0)

    def test_lists_show_only_published_posts(self):
        for url in [self.category.get_absolute_url(), self.tag.get_absolute_url(), '/blog/', '/search/?q=repair']:
            with self.subTest(url=url):
                response = self.client.get(url)
                self.assertContains(response, self.public.title)
                self.assertNotContains(response, self.draft.title)

    def test_sitemap_excludes_drafts(self):
        response = self.client.get('/sitemap.xml')
        self.assertContains(response, self.public.get_absolute_url())
        self.assertNotContains(response, self.draft.get_absolute_url())

    def test_pages_render_without_optional_images(self):
        Comment.objects.create(post=self.public, name='Visitor', email='visitor@example.com',
                               message='A comment', active=True)
        for url in ['/', '/about/', '/price/', '/blog/', self.public.get_absolute_url()]:
            with self.subTest(url=url):
                response = self.client.get(url)
                self.assertEqual(response.status_code, 200)
                self.assertNotContains(response, 'src=""')
                self.assertNotContains(response, 'url()')

    def test_post_image_metadata_only_when_image_exists(self):
        response = self.client.get(self.public.get_absolute_url())
        self.assertNotContains(response, 'property="og:image"')
        Post.objects.filter(pk=self.public.pk).update(main_image='articles/example.webp')
        response = self.client.get(self.public.get_absolute_url())
        self.assertContains(response, 'property="og:image"')
        self.assertContains(response, 'articles/example.webp')

    def test_admin_previews_handle_empty_images(self):
        self.assertEqual(site._registry[Post].get_image(Post()), 'Нет изображения')
        self.assertEqual(site._registry[Image].get_image(Image()), 'Нет изображения')

    def test_unpublishing_hides_post(self):
        self.assertEqual(self.client.get(self.public.get_absolute_url()).status_code, 200)
        Post.objects.filter(pk=self.public.pk).update(status='draft')
        self.assertEqual(self.client.get(self.public.get_absolute_url()).status_code, 404)
        self.assertNotContains(self.client.get('/sitemap.xml'), self.public.get_absolute_url())

    def test_service_pages_use_current_prices(self):
        category = PriceCategory.objects.create(name='Плитка', description='Работы')
        price = Price.objects.create(name='Укладка керамогранита', category=category, price=4200, updated=None)
        url = '/uslugi/plitka-i-keramogranit/'
        self.assertContains(self.client.get(url), '4200')
        Price.objects.filter(pk=price.pk).update(price=4500)
        self.assertContains(self.client.get(url), '4500')
        for slug in SERVICES:
            self.assertEqual(self.client.get('/uslugi/' + slug + '/').status_code, 200)
        self.assertEqual(self.client.get('/uslugi/unknown/').status_code, 404)

    def test_seo_metadata_and_structured_data(self):
        for url in ['/', '/price/', '/about/', '/favorites/', '/blog/']:
            with self.subTest(url=url):
                response = self.client.get(url)
                html = response.content.decode()
                self.assertEqual(html.count('<h1'), 1)
                self.assertEqual(html.count('name="description"'), 1)
                self.assertNotIn('name="description" content=""', html)
                self.assertContains(response, 'rel="canonical" href="https://remont199.com' + url)
                data = json.loads(re.search(r'<script type="application/ld\+json">(.*?)</script>', html).group(1))
                self.assertEqual(data['@type'], 'HomeAndConstructionBusiness')
                self.assertNotIn('telephone', data)

    def test_phone_and_portfolio_details_only_show_real_values(self):
        self.assertNotContains(self.client.get('/'), 'tel:')
        ContactLink.objects.create(name='Телефон', value='+7 (999) 123-45-67')
        response = self.client.get('/')
        self.assertContains(response, 'href="tel:+79991234567"')
        Post.objects.filter(pk=self.public.pk).update(is_favorite=True, project_area=55,
            project_location='Москва', project_duration='2 месяца', project_cost=300000)
        response = self.client.get('/favorites/')
        for value in ['55 м²', 'Москва', '2 месяца', '300000 ₽']:
            self.assertContains(response, value)

    def test_sitemap_includes_public_landing_pages(self):
        response = self.client.get('/sitemap.xml')
        for path in ['/about/', '/price/', '/calc/', *['/uslugi/' + slug + '/' for slug in SERVICES]]:
            self.assertContains(response, path)
        response = self.client.get('/robots.txt')
        self.assertContains(response, 'Sitemap: https://remont199.com/sitemap.xml')
        self.assertTrue(response['Content-Type'].startswith('text/plain'))

    def test_search_pagination_preserves_query(self):
        for index in range(10):
            Post.objects.create(title='Repair result ' + str(index), author=self.author,
                category=self.category, status='published', text='Test')
        self.assertContains(self.client.get('/search/?q=Repair'), 'page=2&amp;q=Repair')
        self.assertContains(self.client.get('/search/?q=Repair'), 'noindex, follow')
