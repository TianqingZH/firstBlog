from django.db import models
from django.contrib.auth.models import User
from django.utils.six import python_2_unicode_compatible
from django.urls import reverse
# Create your models here.
#装饰器用于兼容python2
@python_2_unicode_compatible
class Category(models.Model):
    name=models.CharField(max_length=100)
    def __str__(self):
    	return self.name
@python_2_unicode_compatible
class Tag(models.Model):
	name=models.CharField(max_length=100)
	def __str__(self):
		return self.name
@python_2_unicode_compatible
class Post(models.Model):
	#文章标题
	title=models.CharField(max_length=70)
	#文章正文
	body=models.TextField()
	#文章创建时间及文章的最后一次修改时间，存储时间用DateTime类型
	created_time=models.DateTimeField()
	modified_time=models.DateTimeField()
	#文章摘要，可以没有文章摘要但默认情况下CharField要求我们必须存入数据，否则就会报错。
	#指定 CharField 的 blank=True 参数值后就可以允许空值了。
	excerpt=models.CharField(max_length=200,blank=True)
    #关联一对多ForeignKey 多对多ManyToManyFiled 并由于标签tags指定blank=True,所以文章可以没有标签
	category=models.ForeignKey(Category)
	tags=models.ManyToManyField(Tag,blank=True)
	author=models.ForeignKey(User)
	def __str__(self):
	   	return self.title
	#
	def get_absolute_url(self):
		return reverse('blog:detail',kwargs={'pk':self.pk})#reverse 反向解析blog下的detail视图，并传入
		#并传入关键字参数，即在urls的捕获的pk值,并返回一个post地址




