import sys, os
os.environ['DJANGO_SETTINGS_MODULE'] = 'spectrum.settings'
import settings
from django.conf import settings


from syncr.app.delicious import DeliciousSyncr
d = DeliciousSyncr(settings.DELICIOUS_USER, settings.DELICIOUS_PASS)
d.syncRecent(count=20)

from syncr.app.flickr import FlickrSyncr
f = FlickrSyncr(settings.FLICKR_API_KEY, settings.FLICKR_API_SECRET)
f.syncRecentPhotos('lather rinse repeat', days=60)

from lastfm.lastfm import LastfmSyncr
l=LastfmSyncr()
l.syncposts(user='misstricky', chart='weeklyartistchart')
l.syncposts(user='misstricky', chart='weeklytrackchart')
l.syncposts(user='misstricky', chart='weeklyalbumchart')
l.syncposts(user='misstricky', chart='recentlovedtracks')
l.syncposts(user='misstricky', chart='recenttracks')


from tumblr.tumblr import TumblrSyncr
t=TumblrSyncr()
t.syncposts('missliz')
t.syncposts('didntwrite')


from syncr.app.delicious import DeliciousSyncr
d = DeliciousSyncr(settings.DELICIOUS_USER, settings.DELICIOUS_PASS)
d.syncRecent(count=20)

from syncr.app.flickr import FlickrSyncr
f = FlickrSyncr(settings.FLICKR_API_KEY, settings.FLICKR_API_SECRET)
f.syncRecentPhotos('lather rinse repeat', days=60)

from lastfm.lastfm import LastfmSyncr
l=LastfmSyncr()
l.syncposts(user='misstricky', chart='weeklyartistchart')
l.syncposts(user='misstricky', chart='weeklytrackchart')
l.syncposts(user='misstricky', chart='weeklyalbumchart')
l.syncposts(user='misstricky', chart='recentlovedtracks')
l.syncposts(user='misstricky', chart='recenttracks')


from tumblr.tumblr import TumblrSyncr
t=TumblrSyncr()
t.syncposts('missliz')
t.syncposts('didntwrite')

