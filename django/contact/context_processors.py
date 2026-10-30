import re
import json
from urllib.parse import urlencode

from django.conf import settings
from .models import About, ContactLink
from blog.site_content import SERVICES


def site_context(request):
    about = About.objects.last()
    phone = ''
    phone_href = ''
    links = list(ContactLink.objects.all())
    candidates = [item.value for item in links if re.search(r'phone|тел|звон', item.name, re.I)]
    if about:
        candidates.append(about.slogan)
    for candidate in candidates:
        digits = re.sub(r'\D', '', candidate)
        if len(digits) == 11 and digits[0] in '78':
            phone = candidate
            phone_href = 'tel:+7' + digits[1:]
            break
        if len(digits) == 10:
            phone = candidate
            phone_href = 'tel:+7' + digits
            break
    pages = {
        '/': ('Ремонт квартир в Москве и Московской области — remont199.com', 'Ремонт и отделка квартир в Москве и Московской области. Примеры выполненных работ, цены на отделку и калькулятор предварительной стоимости.'),
        '/about/': ('О нас и контакты — remont199.com', 'Узнайте о работе remont199.com, посмотрите фотографии и свяжитесь с нами для обсуждения ремонта квартиры.'),
        '/price/': ('Цены на ремонт и отделочные работы — remont199.com', 'Расценки на отделку, укладку плитки, декоративную штукатурку и другие ремонтные работы. Рассчитайте предварительную стоимость ремонта.'),
        '/favorites/': ('Наши работы: ремонт и отделка квартир — remont199.com', 'Фотографии и описания выполненных работ по ремонту и отделке. Посмотрите примеры перед обсуждением своего проекта.'),
        '/blog/': ('Блог о ремонте и отделке — remont199.com', 'Материалы о ремонте, отделке и декоративных покрытиях. Практические детали и примеры работ remont199.com.'),
    }
    title, description = pages.get(request.path, ('Ремонт и отделка — remont199.com', 'Ремонт и отделка квартир: работы, цены и полезные материалы remont199.com.'))
    origin = settings.SITE_PUBLIC_URL.rstrip('/')
    canonical = origin + request.path
    page = request.GET.get('page', '')
    if page.isdigit() and int(page) > 1:
        canonical += '?' + urlencode({'page': page})
    business = {'@context': 'https://schema.org', '@type': 'HomeAndConstructionBusiness',
                'name': 'remont199.com', 'url': origin + '/',
                'areaServed': ['Москва', 'Московская область']}
    if phone_href:
        business['telephone'] = phone_href.removeprefix('tel:')
    business_jsonld = json.dumps(business, ensure_ascii=False).replace('<', '\u003C').replace('>', '\u003E').replace('&', '\u0026')
    return {
        'site_phone': phone, 'site_phone_href': phone_href,
        'site_contact_links': links, 'site_about': about,
        'site_services': SERVICES, 'seo_title': title, 'seo_description': description,
        'canonical_url': canonical,
        'sitemap_url': origin + '/sitemap.xml', 'business_jsonld': business_jsonld,
        'seo_noindex': request.path.startswith(('/search/', '/accounts/', '/blog/post-create/', '/contact_us/', '/comment/')),
    }
