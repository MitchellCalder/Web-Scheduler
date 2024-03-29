
"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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

from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import views as auth_views
from django.urls import include, path
from two_factor.urls import urlpatterns as tf_urls


urlpatterns = [
    path(r'', include(tf_urls)),
    path('admin/', admin.site.urls),
    path('webdesignproject/', include('django.contrib.auth.urls')),
    url(r'^login/$', LoginView.as_view(), name='login'),
    path('calendarApp/', include('calendarApp.urls')),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),
    path('', include('calendarApp.urls')),
]
