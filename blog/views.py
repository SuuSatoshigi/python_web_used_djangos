from django.shortcuts import render
from django.utils import timezone
from .models import Post
from .models import Project
from django.shortcuts import render, get_object_or_404
from .forms import PostForm
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required  

# 首页
# return （返回）用 render 方法渲染模板 blog/post_list.html 而得到的结果.
def post_list(request):
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'blog/post_list.html', {'posts':posts})

# 博客内容页
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

# 新建博客文
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('blog.views.post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})
    
# 编辑博文
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('blog.views.post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

#----------------------------------------------------------------------

# 乱入的个人简历
@login_required
def personal_resume(request):
    return render(request, 'blog/personal_resume.html', {})

# 乱入的项目介绍
@login_required
def project_introduction(request):
    projects = Project.objects.filter(is_project_show=True).order_by('order_priority')
    return render(request, 'blog/project_introduction.html', {'projects':projects})