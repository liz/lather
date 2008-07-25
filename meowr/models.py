import datetime
from django.db import models
from django.contrib.auth.models import User
from tagging.fields import TagField
from markdown import markdown
from django.db.models import permalink
from threadedcomments.moderation import moderator, CommentModerator

class Section(models.Model):

	KIND_CHOICES = (
    (1, 'tag'),
    (2, 'rating'),
  )
	title       = models.CharField(max_length=100)
	slug        = models.SlugField(unique=True)
	description = models.CharField(max_length=100)
	kind 		= models.IntegerField(choices=KIND_CHOICES, default=1)

	class Meta:
		verbose_name = 'section'
		ordering = ['title']
  
	def __unicode__(self):
		return self.title
  
	def get_absolute_url(self):
		return self.slug
		
	def live_article_set(self):
		from mewor.models import Aritcle
		return self.article_set.filter(status=Article.LIVE_STATUS)

class Rating(models.Model):
	title       = models.CharField(max_length=100)
	slug        = models.SlugField(unique=True)
	description = models.CharField(max_length=250)

	class Meta:
		verbose_name = 'rating'
		ordering = ['title']
		
	def __unicode__(self):
		return self.title

	def get_absolute_url(self):
		return self.slug
		
	def live_article_set(self):
		from mewor.models import Aritcle
		return self.article_set.filter(status=Article.LIVE_STATUS)
	
class Article(models.Model):
	
	LIVE_STATUS = 1
	DRAFT_STATUS = 2
	HIDDEN_STATUS = 3
	
	STATUS_CHOICES = (
    (1, 'live'),
    (2, 'draft'),
	(3, 'hidden'),
  )
	title 			= models.CharField(max_length=250)
	slug  			= models.SlugField(unique_for_date='pub_date')
	body 			= models.TextField()
	excerpt 		= models.TextField(blank=True)
	pub_date 		= models.DateTimeField(default=datetime.datetime.now)
	cre_date        = models.DateTimeField(auto_now_add=True)
	mod_date        = models.DateTimeField(auto_now=True)
	status 			= models.IntegerField(choices=STATUS_CHOICES, default=1)
	author 			= models.ForeignKey(User, default=1)
	sections		= models.ManyToManyField(Section, default="articles")
	tags			= TagField()
	rating          = models.ManyToManyField(Rating, blank=True)
	enable_comments = models.BooleanField(default=True)
	body_html		= models.TextField(editable=False, blank=True)
	excerpt_html	= models.TextField(editable=False, blank=True)
	
	class Meta:
		verbose_name = 'article'
		ordering = ['-pub_date']
		
	def __unicode__(self):
		return self.title
	
	def save(self):
		self.body_html = markdown(self.body)
		if self.excerpt:
			self.excerpt_html = markdown(self.excerpt)
		super(Article, self).save()
	
	def get_absolute_url(self):
		return ('article_view', (), { 
		'year': self.pub_date.year,
		'month': self.pub_date.month,
		'day': self.pub_date.day,
		'slug': self.slug })
	get_absolute_url = permalink(get_absolute_url)

class Exit(models.Model):
	title       = models.CharField(max_length=100)
	slug        = models.SlugField(unique=True)
	pub_date 	= models.DateTimeField(default=datetime.datetime.now)
	cre_date    = models.DateTimeField(auto_now_add=True)
	mod_date    = models.DateTimeField(auto_now=True)
	url			= models.URLField(unique=True)
	
	class Meta:
	    verbose_name = 'exit'
	    ordering = ['title']
	
	def __unicode__(self):
	    return self.title
	
	def get_absolute_url(self):
		return ('exit_view', (), { 
		'year': self.pub_date.year,
		'month': self.pub_date.month,
		'day': self.pub_date.day,
		'slug': self.slug })
	get_absolute_url = permalink(get_absolute_url)
	
class ArticleModerator(CommentModerator):
	akismet 			= True
	enable_field 		= 'enable_comments'
	email_notification 	= True
	auto_close_field	= 'pub_date'
	close_after			= 30

moderator.register(Article, ArticleModerator)