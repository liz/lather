from django.conf.urls.defaults import *
from meowr.feeds import LatestArtclesFeed, TaggedArticlesFeed, SectionFeed, CommentsFeed
from django.contrib import admin
from django.conf import settings

feeds = {
    'posts': LatestArtclesFeed,
    'tags': TaggedArticlesFeed,
	  'sections': SectionFeed,
	  'comments': CommentsFeed
}

admin.autodiscover()

import mobileadmin
mobileadmin.autoregister()

urlpatterns = patterns('',
    # Example:
    # (r'^lather/', include('lather.foo.urls')),

	 url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

	 url(r'^admin/meowr/article/(?P<object_id>[0-9]+)/preview/$', 'meowr.views.preview'),
	
	 url(r'^admin/(.*)', admin.site.root),
	 
	 url(r'^ma/(.*)', mobileadmin.sites.site.root),
	
     #url(r'^admin/', include('django.contrib.admin.urls')),

	 url(r'^feeds/(?P<url>.*)/$', 'django.contrib.syndication.views.feed', { 'feed_dict': feeds }, name='feeds'),

	 url(r'^(?P<url>(girl|site)/)$', 'django.contrib.flatpages.views.flatpage'), 
	
	 url(r'^threadedcomments/', include('threadedcomments.urls')),
	
	 url (r'^search/$', 'search.views.search'),

	 url(r'^', include('meowr.urls')),
	 
)


handler404 = 'mobileadmin.views.page_not_found'
handler500 = 'mobileadmin.views.server_error'

if settings.DEBUG:
	 urlpatterns += patterns('',
	 url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': '/Library/Python/2.5/site-packages/spectrum/static'}),
)