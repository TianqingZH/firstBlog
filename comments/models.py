from django.db import models
from django.utils.six import python_2_unicode_compatible
# Create your models here.
#创建装饰器用于兼容python2
@python_2_unicode_compatible
class Comment(models.Model):
	"""docstring for Comment"""
	name=models.CharField(max_length=100)
	email=models.EmailField(max_length=255)
	url=models.URLField(blank=True)
	text=models.TextField()#用户发表内容
	created_time=models.DateTimeField(auto_now_add=True)#系统自动记录用户的发表评论的时间

	post=models.ForeignKey('blog.Post')#关联到某篇文章（Post）的

	def __str__(self):
		return self.text[:20]

