from django import template
from django.db.models import Count

from blog.models import Category, Post, Tag, Comment

register = template.Library()


@register.simple_tag(name='get_cats')
def get_list_category():
    """Вывод всех категорий"""
    return Category.objects.all()


@register.simple_tag(name='three_last_posts')
def get_three_last_posts():
    """
    загрузить в шаблон {% load menu_tags%}
    {% three_last_posts as  last_posts %}
    <p>{{  last_posts.title }}</p>
    """
    return Post.objects.filter(status='published').select_related('category', 'author')[:3]


@register.simple_tag(name='tag_list')
def get_all_tags():
    """
    загрузить в шаблон {% load menu_tags%}
    {% three_last_posts as  last_posts %}
    <p>{{  last_posts.title }}</p>
    """
    # список тегов, в которых есть посты
    return Tag.objects.annotate(posts_count=Count("post")).filter(posts_count__gt=0)


# @register.inclusion_tag('blog/include/tags/tag_cats_list.html')
# # @register.inclusion_tag('blog/post_detail.html')
# def show_categories():
#     # список категорий, в которых есть посты
#     cats = Category.objects.annotate(posts_count=Count("post")).filter(posts_count__gt=0)
#     return {"cats": cats}


@register.simple_tag(name='not_empty_cats')
# @register.inclusion_tag('blog/post_detail.html')
def get_not_empty_cats():
    # список категорий, в которых есть посты
    return Category.objects.annotate(posts_count=Count("post")).filter(posts_count__gt=0)

