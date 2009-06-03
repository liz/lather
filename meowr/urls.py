from django.conf.urls.defaults import *
from tagging.models import Tag
from tagging.views import tagged_object_list
from tagging.templatetags import tagging_tags
from meowr.models import *

article_info_dict = {
	'queryset':	 Article.live.all(),
	'date_field': 'pub_date',
	'month_format': '%m',
}

article_list_dict = {
	'queryset':	 Article.live.all(),
	'paginate_by': 1,
}

urlpatterns = patterns('django.views.generic',
    # Example:
    # (r'^lather/', include('lather.foo.urls')),

	 url(r'^(?P<year>\d{4})/(?P<month>\d{1,2})/(?P<day>\d{1,2})/(?P<slug>[a-z0-9_-]+)/$',
	  'date_based.object_detail', 
	  dict(article_info_dict, 
	  slug_field='slug'), 
	  name='article_view'
	  ),
	
	url(r'^plain/(?P<year>\d{4})/(?P<month>\d{1,2})/(?P<day>\d{1,2})/(?P<slug>[a-z0-9_-]+)/$',
	  'date_based.object_detail', 
	  dict(article_info_dict,
	  slug_field='slug', 
	  template_name='meowr/article_detail_plain.html'), 
	  name='article_view_plain'
	  ),

	 url(r'^(?P<year>\d{4})/(?P<month>\d{1,2})/(?P<day>\d{1,2})/$',
	  'date_based.archive_day', 
	  article_info_dict, 
	  name='day_view'
	  ),

	 url(r'^(?P<year>\d{4})/(?P<month>\d{1,2})/$',
	  'date_based.archive_month', 
	   article_info_dict, 
	   name='month_view'
	   ),

	 url(r'^(?P<year>\d{4})/$',
	  'date_based.archive_year', 
	  dict(queryset=Article.live.all(), 
	  date_field='pub_date'), 
	  name='year_view'
	  ),
 
	 url(r'^$', 
	 'list_detail.object_list', 
	 article_list_dict, 
	 name='article_index'
	 ),
	
	 url(r'^exits/$', 
	 'list_detail.object_list',  
	 dict(queryset=Exit.objects.order_by('-tags', 'title'), 
	 paginate_by=100), 
	 name='exit_list'
	 ),
	
	 url(r'^tags/$', 'list_detail.object_list', 
	 dict(queryset=Tag.objects.all(), 
	 paginate_by=100, 
	 template_name='meowr/tag_list.html')
	 ),
	
	 url(r'^ratings/$', 
	 'list_detail.object_list', 
	 dict(queryset=Rating.objects.all(), 
	 paginate_by=100), 
	 name='rating_list'
	 ),
	
	 url(r'^tags/(?P<tag>[^/]+)/$', 
	 tagged_object_list, 
	 dict(queryset_or_model=Article.live.all(), 
	 paginate_by=10, 
	 allow_empty=True, 
	 template_name='meowr/article_tag_detail.html'), 
	 name='article_tag_detail.html'
	 ),
	
)

urlpatterns += patterns('meowr.views',
	
	url(r'^(?P<slug>[a-z0-9_-]+)/$', 
	'section_detail'),
	
	url(r'^ratings/(?P<slug>[a-z0-9_-]+)/$', 
	'rating_detail'),
)