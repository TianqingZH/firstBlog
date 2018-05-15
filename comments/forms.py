from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
	"""docstring for CommentForm"""
	class Meta:#表单内部类
		"""docstring for Meta"""
		model=Comment#表单对应的数据库模型是Comment类
		fields=['name','email','url','text']#指定了表单要显示的字段
	#内部类
	'''
		class parent:
10 
11     			def __init__(self):
12         			self.name = "parent"
13 
14     			def getName(self):
15         			print self.name
16 
17     			class child:
18 
19         			def __init__(self):
20             			self.name = "child"
21 
22         			def getName(self):
23             			print self.name
24 
25 		if __name__ == "__main__":
26     		# child = parent.child()
27     		# child.getName()
28 
29     		p = parent()
30     		p.getName()
31 
32     		print "================="
33     		c = p.child()
34     		c.getName()
	'''