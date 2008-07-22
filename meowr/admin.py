from django.contrib import admin
from meowr.models import Article, Exit, Section, Rating
from tagging.models import Tag, TaggedItem

class ArticleAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug': ('title',)} 
	list_display  = ('title', 'pub_date', 'status')
	list_filter   = ('pub_date', 'sections', 'status', 'rating')
	search_fields = ('title', 'body', 'status', 'tags')

class ExitAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug': ('title',)}
	search_fields = ('title',)
	
class SectionAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug': ('title',)} 

class RatingAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug': ('title',)}

admin.site.register(Article, ArticleAdmin)
admin.site.register(Section, SectionAdmin)
admin.site.register(Rating, RatingAdmin)
admin.site.register(Exit, ExitAdmin)
admin.site.register(Tag)
admin.site.register(TaggedItem)