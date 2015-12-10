from django.shortcuts import render
from django.utils import timezone
from .models import Post

# return （返回）用 render 方法渲染模板 blog/post_list.html 而得到的结果.
def post_list(request):
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'blog/post_list.html', {'posts':posts})
