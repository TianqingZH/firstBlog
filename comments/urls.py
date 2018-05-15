from django.conf.urls import url

from .import views

app_name='comments'
urlpatterns=[
	#$以什么结尾
	url(r'^comment/post/(?P<post_pk>[0-9]+)/$',views.post_comment,name='post_comment'),
]