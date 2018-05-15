import markdown
from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from comments.forms import CommentForm
from .models import Post,Category
# Create your views here.
#render (访问网址，模板文件地址，)
def  index(request):
	post_list=Post.objects.all()#.order_by('-created_time')
	return render(request,'blog/index.html',context={
		'title':'我的博客主页',
		'post_list':post_list,
		})
def detail(request,pk):
	#当传入的 pk 对应的 Post 在数据库存在时，就返回对应的 post文章，如果不存在，就给用户返回一个 404 错误
	post=get_object_or_404(Post,pk=pk)
	#extensions 它是对 Markdown 语法的拓展，extra 本身包含很多拓展，而 codehilite 是语法高亮拓展，这为我们后面的实现代码高亮功能提供基础，而 toc 则允许我们自动生成目录
	post.body=markdown.markdown(post.body,
								extensions=[
									'markdown.extensions.extra',
									'markdown.extensions.codehilite',
									'markdown.extensions.toc'
								])
	form=CommentForm()
	comment_list=post.comment_set.all()
	#context 参数的值把模板中的变量替换为我们传递的变量的
	context={
				'post':post,
				'form':form,
				'comment_list':comment_list
	}
	return render(request,'blog/detail.html',context=context)
#通过模型管理器的filter来过滤，指定参数，created_year created_month来过滤，在django中，要将python中的created_time.year用created_time__year表示，再排序
def archives(request,year,month):
	post_list=Post.objects.filter(created_time__year=year,
								  created_time__month=month
								  )#.order_by('-created_time')
	return render(request,'blog/index.html',context={'post_list':post_list})
#分类界面视图函数
def category(request,pk):
	cate=get_object_or_404(Category,pk=pk)
	post_list=Post.objects.filter(category=cate)#.order_by('-created_time')
	return render(request,'blog/index.html',context={'post_list':post_list})
