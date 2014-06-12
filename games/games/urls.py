from django.conf.urls import patterns, include, url
from django.views.generic import UpdateView, DeleteView
from igames.views import *
from rest_framework.urlpatterns import format_suffix_patterns

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

    url(r'^login/$','django.contrib.auth.views.login'),
    url(r'^logout/$','django.contrib.auth.views.logout', {'next_page':'/'}),

    url(r'^register/$', register),

    url(r'^mygames(.*)/$', mygamespage),
    ###############################################################
    url(r'^games/create/$', GameCreate.as_view(success_url="/")), 
    url(r'^games/(?P<slug>\w+)/edit/$', GameEdit.as_view(
				slug_field ='name',
				success_url="/")),  
    url(r'^games/(?P<slug>\w+)/delete/$', GameDelete.as_view(
				slug_field ='name',
				success_url="/")), 

    url(r'^companies/create/$', CompanyCreate.as_view(success_url="/")), 
    url(r'^companies/(?P<slug>\w+)/edit/$', CompanyEdit.as_view(
				slug_field ='name',
				success_url="/")),  
    url(r'^companies/(?P<slug>\w+)/delete/$', CompanyDelete.as_view(
				slug_field ='name',
				success_url="/")), 

    url(r'^platforms/create/$', PlatformCreate.as_view(success_url="/")), 
    url(r'^platforms/(?P<slug>\w+)/edit/$', PlatformEdit.as_view(
				slug_field ='name',
				success_url="/")),  
    url(r'^platforms/(?P<slug>\w+)/delete/$', PlatformDelete.as_view(
				slug_field ='name',
				success_url="/")),

    url(r'^games/(\w+)/reviews/create/$',
        review,
        name='review_create'),
    ###############################################################

    url(r'^developers/(\w+)(.*)/$', userpage),
    url(r'^developers(.*)/$', userspage),

    url(r'^games/(\w+)(.*)/$', gamepage),
    url(r'^games(.*)/$', gamespage,name = 'game_detail'),

    url(r'^companies/(\w+)(.*)/$', companypage),
    url(r'^companies(.*)/$', companiespage),

    url(r'^platforms/(\w+)(.*)/$', platformpage),
    url(r'^platforms(.*)/$', platformspage),


    url(r'^api/developers/(?P<username>\w+)/$', APIDeveloperDetail.as_view(),name = 'user-detail'),
    url(r'^api/developers/$', APIDeveloperList.as_view(),name = 'user-list'),

    url(r'^api/games/(?P<name>\w+)/$',APIGameDetail.as_view(),name = 'game-detail'),
    url(r'^api/games/$', APIGameList.as_view(),name = 'game-list'),

    url(r'^api/companies/(?P<name>\w+)/$', APICompanyDetail.as_view(),name = 'company-detail'),
    url(r'^api/companies/$', APICompanyList.as_view(),name = 'company-list'),

    url(r'^api/platforms/(?P<name>\w+)/$', APIPlatformDetail.as_view(),name = 'platform-detail'),
    url(r'^api/platforms/$', APIPlatformList.as_view(),name = 'platform-list'),
)

urlpatterns = format_suffix_patterns(urlpatterns, allowed=['api' ,'json', 'xml'])
