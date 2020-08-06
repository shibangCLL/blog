from django.shortcuts import render, get_object_or_404

from .models import Article, Carousel, AboutAuthor, Category

from django.core.paginator import Paginator


# Create your views here.
# 视图函数
def article_list(request):
    articles = Article.objects.all()

    # paginator = Paginator(articles, 4)
    # # 获取 url 中的页码
    # page = request.GET.get('page')
    # # 将导航对象相应的页码内容返回给 articles
    #
    # articles = paginator.page(page)

    carousels = Carousel.objects.all()
    articles_top = Article.objects.all().filter(is_top=True)
    author = AboutAuthor.objects.get(name='Chenglulu')
    context = {'articles': articles, 'carousels': carousels, 'articles_top': articles_top, 'author': author}
    return render(request, 'my_blog2/index.html', context)


def article_detail(request, id):
    # 取出相应的文章
    article = Article.objects.get(id=id)
    article.update_views()
    article.body = article.body_to_markdown()
    # 需要传递给模板的对象
    context = {'article': article}
    # 载入模板，并返回context对象
    return render(request, 'my_blog2/table.html', context)


def category(request, pk):
    # 记得在开始部分导入 Category 类
    cate = get_object_or_404(Category, pk=pk)
    category_list = Category.objects.filter(category=cate).order_by('-created_time')
    return render(request, 'my_blog2/index.html', context={'post_list': category_list})
