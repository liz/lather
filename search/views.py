from django.shortcuts import get_object_or_404, render_to_response
from django.http import HttpResponse
from django.template import loader, Context
from meowr.models import Article
from django.db.models import Q

def search(request):
	query = request.GET.get('q', '')
	if query:
		qset = (
			Q(title__icontains=query) |
			Q(body__icontains=query) |
			Q(excerpt__icontains=query) |
			Q(tags__icontains=query)
		)
		results = Article.objects.filter(qset, status=Article.LIVE_STATUS).distinct()
	else:
		results = []
	return render_to_response('search/search.html', {
		'results': results,
		'query': query,
	})