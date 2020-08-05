from django.shortcuts import render

from .models import Article, Carousel, AboutAuthor


# Create your views here.
# 视图函数
def article_list(request):
    articles = Article.objects.all()
    carousels = Carousel.objects.all()
    articles_top = Article.objects.all().filter(is_top=True)
    authors = AboutAuthor.objects.all()
    context = {'articles': articles, 'carousels': carousels, 'articles_top': articles_top, 'authors': authors}
    return render(request, 'my_blog2/index.html', context)


def article_detail(request, id):
    # 取出相应的文章
    article = Article.objects.get(id=id)
    article.body = article.body_to_markdown()
    # 需要传递给模板的对象
    context = { 'article': article }
    # 载入模板，并返回context对象
    return render(request, 'my_blog2/table.html', context)