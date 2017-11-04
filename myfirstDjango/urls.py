"""myfirstDjango URL Configuration

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

from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import urls as auth_urls
from blog import views as blog_views


urlpatterns = [
    url(r'^account/',include(auth_urls,namespace='users.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('users.urls')),
    url(r'^ajax_list/$', blog_views.json_list, name='ajax-list'),
    url(r'^ajax_dict/$', blog_views.json_dict, name='ajax-dict'),
    url(r'^mine/$',blog_views.MyView.as_view(),name='my-view')
]
