from django.core.exceptions import ObjectDoesNotExist
from django.utils.feedgenerator import Atom1Feed
from django.contrib.sites.models import Site
from django.contrib.syndication.feeds import Feed
from meowr.models import Article, Section
from tagging.models import Tag, TaggedItem
from threadedcomments.models import FreeThreadedComment

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
		
class CommentsFeed(Feed):
	author_name			= "Liz"
	copyright			= "Liz"
	description			= "Latest comments posted on Lather Rinse Repeat"
	item_copyright		= "Liz"
	item_author_name	= "Liz"
	link				= "/comments/"
	item_link = link
	title				= "Lather Rinse Repeat"
	feed_type			= Atom1Feed
	feed_guid 			= "/feeds/comments/"
	
	def items(self):
		return FreeThreadedComment.objects.all()[:15]
		
	def item_pubdate(self, item):
		return item.date_submitted
		
		
class TaggedArticlesFeed(Feed):
	def get_object(self, bits):
		tag = Tag.objects.get(name=bits[0])
		return tag

	def items(self, obj):
		return TaggedItem.objects.get_by_model(Article.objects.filter(status=Article.LIVE_STATUS), obj)[:15]

	def link(self, obj):
		return '/tags/%s/' % obj

	def title(self, obj):
		return 'Lather Rinse Repeat - Tag %s' % obj

	def description(self, obj):
		return 'Lather Rinse Repeat - Tag %s' % obj
		
	def item_pubdate(self, item):
		return item.pub_date
		
		
class SectionFeed(Feed):
	def get_object(self, bits):
		section = Section.objects.get(slug=bits[0])
		return section

	def items(self, obj):
		return obj.live_article_set()[:15]

	def link(self, obj):
		return '/%s/' % obj.slug

	def title(self, obj):
		return 'Lather Rinse Repeat - %s' % obj

	def description(self, obj):
		return 'Lather Rinse Repeat - %s' % obj
		
	def item_pubdate(self, item):
		return item.pub_date