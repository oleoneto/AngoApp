"""AngoApp URL Configuration

EKLETIK URL Configuration
Written by Leo Neto
Updated on Sept 16, 2017

"""

# Importing Django stuff...
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.contrib.auth.models import User
from django.contrib.auth.views import *
from django.conf import settings
from django.conf.urls.static import static

# Importing application views
from Website import views as site
from Website import APIViews as API
from Website import search as search

# Importing REST API
from rest_framework import routers, serializers, viewsets
from rest_framework.urlpatterns import format_suffix_patterns

# admin.autodiscover()


urlpatterns = [
    # Admin / Auth / Status Code Views
    url(r'^401', site.error_401, name='401'),
    url(r'^403', site.error_403, name='403'),
    url(r'^404', site.error_404, name='404'),
    url(r'^405', site.error_405, name='405'),
    url(r'^500', site.error_500, name='500'),
    url(r'^admin.*', site.error_404),
    url(r'^dash.*', site.error_404),
    url(r'^wp.*', site.error_404),
    url(r'^login.*', site.error_404),

    # ------------------
    # Login and Logout Views
    url(r'^i/sys/', admin.site.urls, name='sys'),
    url(r'^i/logout/$', logout, {'template_name': 'masters/logout.html'}, name='logout'),
    url(r'^i/login/$', site.userlogin, name='userlogin'),
    url(r'^i/auth/$', site.userauth, name='userauth'),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # -------------------


    # MAIN Views
    url(r'^$', site.home, name='home'),
    url(r'^portfolio/(?P<keyword>\D+)', site.project_detail, name='portfolio-detail'),
    url(r'^portfolio/', site.projects, name='portfolio'),
    url(r'^about/', site.about, name='about'),
    url(r'^services/', site.services, name='services'),
    url(r'^process/', site.process, name='process'),
    url(r'^blog/(?P<keyword>\D+)', site.article_single, name='blog-single'),
    url(r'^blog/', site.articles, name='blog'),
    url(r'^articles/', site.articles, name='articles'),

    # SEARCH
    url(r'^p/', search.SearchViewController, name='search'),

    #--------------

    # API Views
    url(r'^api/people/(?P<pk>\d+)', API.PersonDetailAPIView.as_view()),
    url(r'^api/people', API.PersonListAPIView.as_view()),

    url(r'^api/projects/(?P<pk>\d+)', API.ProjectDetailAPIView.as_view()),
    url(r'^api/projects/(?P<slug>\D+)', API.ProjectDetailAPIViewSlug.as_view()),
    url(r'^api/projects', API.ProjectListAPIView.as_view()),

    #--------------

    # REDIRECT Views
    url(r'^youtube', site.azinca),
    url(r'^ekletik', site.ekletik),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# REST API URL Configuration...
urlpatterns = format_suffix_patterns(urlpatterns)