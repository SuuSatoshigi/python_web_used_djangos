# from django.conf.urls import url
from . import views
from django.conf.urls import patterns, include, url

urlpatterns = [
	url(r'^$',views.post_list,name='post_list'),
	url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
	url(r'^post/new/$', views.post_new, name='post_new'),
	url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
	url(r'^personal_resume/$', views.personal_resume, name='personal_resume'),
	url(r'^personal_resume/project_introduction/$', views.project_introduction, name='project_introduction'),
	url(r'^accounts/login/$', 'django.contrib.auth.views.login', {'template_name': 'blog/login.html'}),
]