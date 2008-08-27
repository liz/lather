from django.shortcuts import get_object_or_404, render_to_response
from django.views.generic import date_based, list_detail
from django.views.generic.list_detail import object_list, object_detail
from tagging.views import tagged_object_list
from tagging.models import Tag
from meowr.models import *
from tagging.templatetags import tagging_tags
from django.contrib.admin.views.decorators import staff_member_required

def section_detail(request, slug):
	section = get_object_or_404(Section, slug=slug)
	return object_list(request, queryset=section.article_set.filter(status=Article.LIVE_STATUS),
	paginate_by=35, extra_context={ 'section': section, }, template_name = 'meowr/section_detail.html',)
	
def rating_detail(request, slug):
	rating = get_object_or_404(Rating, slug=slug)
	return object_list(request, queryset=rating.article_set.filter(status=Article.LIVE_STATUS),
	paginate_by=10, extra_context={ 'rating': rating }, template_name = 'meowr/article_rating_detail.html',)
	
@staff_member_required
def preview(request, object_id):
	return object_detail(request, object_id=object_id, queryset=Article.objects.all(), )