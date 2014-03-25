from django.conf.urls import patterns, include, url

from igames.views import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'games.views.home', name='home'),
    # url(r'^games/', include('games.foo.urls')),
    

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', mainpage, name='home'),
    url(r'^user/(\w+)/$', userpage),
    url(r'^companies/', companiespage),
    url(r'^games/', gamespage),
    url(r'^platforms/', platformspage),
    url(r'^company/(\w+)/$', companypage),
    url(r'^game/(\w+)/$', gamepage),
    url(r'^platform/(\w+)/$', platformpage),

)