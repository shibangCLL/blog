from django.contrib import admin

# Register your models here.
from .models import Article,Category,Tag,Keyword,Carousel,AboutAuthor

# 注册ArticlePost到admin中
admin.site.register(Article)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Keyword)
admin.site.register(Carousel)
admin.site.register(AboutAuthor)
