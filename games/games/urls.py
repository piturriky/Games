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
	
    url(r'^developers/$', userspage),
    url(r'^companies/$', companiespage),
    url(r'^games/$', gamespage),
    url(r'^platforms/$', platformspage),

    url(r'^companies/(\w+)/$', companypage),
    url(r'^games/(\w+)/$', gamepage),
    url(r'^platforms/(\w+)/$', platformpage),
    url(r'^developers/(\w+)/$', userpage),

    url(r'^login/$','django.contrib.auth.views.login'),
    url(r'^logout/$','django.contrib.auth.views.logout', {'next_page':'/'}),

    url(r'^register/$', register),

	# Formats xml i json
  
    # Llistar developers
    url(r'^developers.json/$', userspagejson),
    url(r'^developers.xml/$', userspagexml),

    # Llistar companies
    url(r'^companies.json/$', companiespagejson),
    url(r'^companies.xml/$', companiespagexml),

    # Llistar games
    url(r'^games.json/$', gamespagejson),
    url(r'^games.xml/$', gamespagexml),

    # Llistar platforms
    url(r'^platforms.json/$', platformspagejson),
    url(r'^platforms.xml/$', platformspagexml),

    url(r'^companies/(\w+).json/$', companypagejson),
    url(r'^companies/(\w+).xml/$', companypagexml),

    url(r'^games/(\w+).json/$', gamepagejson),
    url(r'^games/(\w+).xml/$', gamepagexml),

    url(r'^platforms/(\w+).json/$', platformpagejson),
    url(r'^platforms/(\w+).xml/$', platformpagexml),

    url(r'^developers/(\w+).json/$', userpagejson),
    url(r'^developers/(\w+).xml/$', userpagexml),

)
