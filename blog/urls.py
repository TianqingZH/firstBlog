from django.conf.urls import url
from . import views
#告诉django这个urls.py是属于应用blog的
app_name='blog'
#处理网址和处理函数
#绑定关系的写法是把网址和对应的处理函数作为参数传给 url 函数（第一个参数是网址，第二个参数是处理函数）
urlpatterns=[
	#用户访问不同网址时，如何处理这些不同的网址，Django做法是把不同的网址对应的处理函数写在一个urls.py文件里，当用户访问某个网址时，Django在这个文件里找，如果找到这个网址，就会调用和它绑定在一起的处理函数即视图函数
	url(r'^$',views.index,name='index'),
	#(?P<pk>[0-9]+) 表示命名捕获组，其作用是从用户访问的 URL 里把括号内匹配的字符串捕获并作为关键字参数传给其对应的视图函数 detail。
	#命名捕获组https://blog.csdn.net/lxcnn/article/details/4146148  http://www.jb51.net/article/69644.htm
	url(r'^post/(?P<pk>[0-9]+)/$',views.detail,name='detail'),
	url(r'^archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$',views.archives,name='archives'),
	url(r'^category/(?P<pk>[0-9]+)/$',views.category,name='category')
]