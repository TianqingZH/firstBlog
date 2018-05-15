from django import template#导入template类
from ..models import Post,Category

#实例化template.Librasy类
register = template.Library()
#最新文章标签
#将函数get_recent_posts装饰为register.simple_tag,这样可以在模板中使用语法{% get_recent_posts%}调用这个函数了
#注册这个函数为模板标签，并取前num个
@register.simple_tag
def get_recent_posts(num=5):
	return Post.objects.all().order_by('created_time')[:num]

#归档模板标签（按月归档）
#三个参数：创建时间，month表示精度，order=DESC表示降序排列
@register.simple_tag
def archives():
	return Post.objects.dates('created_time','month',order='DESC')

#分类模板标签
@register.simple_tag
def get_categories():
	return Category.objects.all()



