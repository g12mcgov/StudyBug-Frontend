from django.conf.urls import patterns, include, url
from django.http import HttpResponseRedirect

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^/', include('studybug.urls')),
    url(r'^studybug/', include('studybug.urls')),
    url(r'^$', lambda r: HttpResponseRedirect('studybug/')),
)
