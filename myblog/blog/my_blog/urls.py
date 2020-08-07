# 引入path
from django.urls import path
# 引入views.py
from . import views

# 正在部署的应用的名称
app_name = 'my_blog'

urlpatterns = [
path('article-list/', views.article_list, name='article_list'),
path('article-detail/<int:id>/', views.article_detail, name='article_detail'),
path('categories/<int:pk>/', views.category, name='category'),
path('archives/<int:year>/<int:month>/', views.archive, name='archive'),
path('tags/<int:pk>/', views.tag, name='tag'),
path('search/', views.search, name='search'),
path('time-line/', views.time_line, name='time_line'),
]
