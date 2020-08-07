from django import template

from ..models import Article, Category, Tag

register = template.Library()


@register.inclusion_tag('my_blog2/inclusions/_recent_posts.html', takes_context=True)
def show_recent_posts(context, num=5):
    return {
        'recent_post_list': Article.objects.all().order_by('-create_date')[:num],
    }


@register.inclusion_tag('my_blog2/inclusions/_tags.html', takes_context=True)
def show_tags(context):
    return {
        'tag_list': Tag.objects.all(),
    }


@register.inclusion_tag('my_blog2/inclusions/_archives.html', takes_context=True)
def show_archives(context):
    return {
        'date_list': Article.objects.dates('create_date', 'month', order='DESC'),
    }


@register.inclusion_tag('my_blog2/inclusions/_author_recommend.html', takes_context=True)
def show_author_recommend(context, num=5):
    return {
        'rauthor_recommend_list': Article.objects.all().filter(is_top=True).order_by('-create_date')[:num],
    }


@register.inclusion_tag('my_blog2/inclusions/_hot_article.html', takes_context=True)
def show_hot_article(context, num=5):
    return {
        'hot_article_list': Article.objects.all().order_by('-views')[:num],
    }


@register.inclusion_tag('my_blog2/inclusions/_categories.html', takes_context=True)
def show_categories(context, num=5):
    return {
        'category_list': Category.objects.all(),
    }


@register.inclusion_tag('my_blog2/inclusions/_categories_banner.html', takes_context=True)
def show_categories_banner(context, num=5):
    return {
        'category_list': Category.objects.all(),
    }
