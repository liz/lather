from django.core.exceptions import ObjectDoesNotExist
from django.utils.feedgenerator import Atom1Feed
from django.contrib.sites.models import Site
from django.contrib.syndication.feeds import Feed
from meowr.models import Article

current_site = Site.objects.get_current()

class LatestArtclesFeed(Feed):
	author_name			= "Liz"
	copyright			= "Liz"
	description			= "Latest articles posted to Lather Rinse Repeat"
	item_copyright		= "Liz"
	item_author_name	= "Liz"
	link				= "/"
	title				= "Lather Rinse Repeat"
	feed_type			= Atom1Feed
	feed_guid 			= "/feeds/all-posts/"
	
	def items(self):
		return Article.objects.filter(status=Article.LIVE_STATUS)[:15]
		
	def item_pubdate(self, item):
		return item.pub_date