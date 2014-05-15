from django.conf.urls import patterns, include, url
from django.views.generic import UpdateView, DeleteView
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

    url(r'^developers/(\w+)(.*)/$', userpage),
    url(r'^developers(.*)/$', userspage),

    url(r'^games/(\w+)(.*)/$', gamepage),
    url(r'^games(.*)/$', gamespage),

    url(r'^companies/(\w+)(.*)/$', companypage),
    url(r'^companies(.*)/$', companiespage),

    url(r'^platforms/(\w+)(.*)/$', platformpage),
    url(r'^platforms(.*)/$', platformspage),

    url(r'^login/$','django.contrib.auth.views.login'),
    url(r'^logout/$','django.contrib.auth.views.logout', {'next_page':'/'}),

    url(r'^register/$', register),

    url(r'^mygames(.*)/$', mygamespage),

    url(r'^creategame/$', GameCreate.as_view(success_url="/")), #ARREGLAR URL 
    url(r'^editgame/(?P<slug>\w+)/$', UpdateView.as_view(
				slug_field ='name',
				model = Game,
				template_name = 'formedit.html',
				form_class = GameForm,
				success_url="/")), #ARREGLAR URL 
    url(r'^deletegame/(?P<slug>\w+)/$', DeleteView.as_view(
				slug_field ='name',
				model = Game,
				template_name = 'formdelete.html',
				success_url="/")), #ARREGLAR URL 
   url(r'^resources/(.*)/$', resources),

)
