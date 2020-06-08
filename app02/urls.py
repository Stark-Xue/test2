"""test2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from django.conf.urls import url, include

from app02 import views

urlpatterns = [
    #path('admin/', admin.site.urls),
    re_path('index/(\d+)/', views.index, name="indexx"),
    path('login/', views.login),
    path('regist/', views.regist),
    path('home/', views.Home.as_view()),
    #re_path('detail-(\d+).html', views.detail),
    #re_path('detail-(\d+)-(\d+).html', views.detail),
    #re_path('detail-(?P<nid>\d+)-(?P<uid>\d+).html', views.detail),
    re_path('detail-(?P<nid>\d+).html', views.detail),
]