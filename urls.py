# -*- coding:utf-8 -*-

import os

from django.conf.urls.defaults import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
from django.views.generic.simple import direct_to_template
from django.conf import settings

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'vitrine.views.home', name='home'),
    # url(r'^vitrine/', include('vitrine.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', "core.core_views.homepage", name="homepage"),

    # App Home
    url(r'^home/', include("home.urls", namespace="home")),

    # App Home - exemplo de como importar um arquivo url.py de outro app
    #url(r'^home/', include('home.urls', namespace="home")),

)


# Faz o django servir os arquivos estáticos também, como Js, css, imagens...
if settings.DESENVOLVIMENTO:
    urlpatterns += patterns('',
        (r'^media/(.*)$', 'django.views.static.serve',
            {'document_root': os.path.join(settings.PROJECT_PATH, 'media')}),
        (r'^arquivos/(.*)$', 'django.views.static.serve',
            {'document_root': os.path.join(settings.PROJECT_PATH, 'arquivos')}),
    )