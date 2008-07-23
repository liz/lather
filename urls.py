from django.conf.urls.defaults import *
from meowr.feeds import LatestArtclesFeed
from django.contrib import admin
from django.conf import settings

feeds = {'posts': LatestArtclesFeed }

admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^lather/', include('lather.foo.urls')),

	 url(r'^admin/meowr/article/(?P<object_id>[0-9]+)/preview/$', 'meowr.views.preview'),
	
	 url(r'^admin/(.*)', admin.site.root),
	
     #url(r'^admin/', include('django.contrib.admin.urls')),

	 url(r'^(?P<url>(girl|site)/)$', 'django.contrib.flatpages.views.flatpage'), 
	
	 url(r'^threadedcomments/', include('threadedcomments.urls')),
	
	 url (r'^search/$', 'search.views.search'),

	 url(r'^', include('meowr.urls')),
	
	 url(r'^feeds/(?P<url>.*)/$', 'django.contrib.syndication.views.feed', { 'feed_dict': feeds }),
	
)

if settings.DEBUG:
	 urlpatterns += patterns('',
	 url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': '/Library/Python/2.5/site-packages/lather/static'}),
)