from django.contrib import admin
from meowr.models import Article, Exit, Section, Rating
from tagging.models import Tag, TaggedItem

class ArticleAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug': ('title',)} 
	list_display  = ('title', 'pub_date', 'status')
	list_filter   = ('pub_date', 'sections', 'status', 'rating')
	search_fields = ('title', 'body', 'status', 'tags')
	fieldsets 	  = (
		(None, {
			'fields': ('title', 'slug')
		}),
		('Excerpt', {
			'fields': ('excerpt',),
			'classes': ('collapse',)
		}),
		(None, {
			'fields': ('body',),
		}),
		(None, {
			'fields': ('status', 'author', 'pub_date', 'enable_comments', 'tags',  'sections', 'rating')
		})
	)
	
	def formfield_for_dbfield(self, db_field, **kwargs):
		field = super(ArticleAdmin, self).formfield_for_dbfield(db_field, **kwargs) # Get the default field
		if db_field.name == "body": 
			field.widget.attrs['cols'] = "65"
			field.widget.attrs['rows'] = "18"
		if db_field.name == "excerpt": 
			field.widget.attrs['cols'] = "65"
			field.widget.attrs['rows'] = "14"
		if db_field.name == "title": 
			field.widget.attrs['size'] = "35"
		if db_field.name == "slug":
			field.widget.attrs['size'] = "35"
		return field
		
		
class ExitAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug': ('title',)}
	search_fields = ('title', 'tags')
	
class SectionAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug': ('title',)} 

class RatingAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug': ('title',)}

admin.site.register(Article, ArticleAdmin)
admin.site.register(Section, SectionAdmin)
admin.site.register(Rating, RatingAdmin)
admin.site.register(Exit, ExitAdmin)