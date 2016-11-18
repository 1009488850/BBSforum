"""BBSFunction URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from BBS import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index,name="index"),
    url(r'^category/(\d+)/$', views.category,name="category"),
    url(r'^article/(\d+)/$',views.article_detail,name='article_detail'),
    url(r'^create_article/new/$',views.create_article,name='create_article'),
    url(r'^account/is_logout/',views.acc_logout,name='is_logout'),
    url(r'^account/is_login/',views.acc_login,name='is_login'),
    url(r'^comment/$',views.comment_post,name='post_comment'),

]
