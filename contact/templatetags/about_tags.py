from django import template
from contact.models import *
register = template.Library()


@register.simple_tag()
def get_social_links():
    """Вывод ссылок соц сетей"""
    return Social.objects.all()


@register.simple_tag()
def get_about():
    """
    загрузить в шаблон {% load about_tags%}
    {% get_about as  about %}
    <p>{{  about.slogan }}</p>
    """
    return About.objects.last()


@register.inclusion_tag('contact/include/tags/tag_about_intro.html')
def get_promo():
    """Вывод promo about"""
    intro_about = About.objects.all().first()
    promo = PromoAbout.objects.all()
    img_about = ImageAbout.objects.all()
    return {
            # {{ intro_about }} имя в шаблоне
            "intro_about": intro_about,
            "promo": promo,
            'img_about': img_about,
            }


@register.inclusion_tag('contact/include/tags/tag_about_intro.html')
def another_promo():
    pass
