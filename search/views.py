from django.http import HttpResponse
from django.template import loader, Context
from meowr.models import Article

def search(request):
	query		= request.GET['q']
	results		= Article.live.filter(body__icontains=query)
	template 	= loader.get_template('search/search.html')
	context		= Context({'query': query, 'results': results})
	response	= template.render(context)
	return HttpResponse(response)
	
	