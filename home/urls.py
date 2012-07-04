# -*- coding:utf-8 -*-
#Autor:guerra
#Data: 04/02/12
#Ultima alteracao:

# URLs do app Home

from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('',


    url(r'^$', "home.home_views.homepage", name="homepage"),


)