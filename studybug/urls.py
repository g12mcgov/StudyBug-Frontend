from django.conf.urls import patterns, url
from django.conf import settings
from studybug import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^$/', views.index, name='index'),
        )
