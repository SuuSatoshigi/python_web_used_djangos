from django.db import models
from django.utils import timezone

#博文模型
class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

#项目模型
class Project(models.Model):
    #项目作者
    project_author = models.ForeignKey('auth.User')
    #项目logo+项目名称
    project_name = models.TextField()
    #项目架构+项目架构设计图
    project_scaffold_text = models.TextField(blank=True, null=True)
    #项目完成功能
    project_self_function = models.TextField(blank=True, null=True)
    #项目所用技术介绍
    project_skill = models.TextField(blank=True, null=True)
    #项目链接
    project_url = models.URLField(blank=True, null=True)
    #项目截图
    project_cut = models.TextField(blank=True, null=True)
    #是否显示该项目
    is_project_show = models.BooleanField()
    #显示优先级
    order_priority = models.IntegerField(default=1)

    def show_project(self):
        self.is_project_show = True
        self.save()

    def __str__(self):
        return self.project_name
        