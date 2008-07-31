from django import template
from django.conf import settings
from django.core import template_loader
from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.core.exceptions import ObjectDoesNotExist
from django.utils.safestring import mark_safe
from syncr.twitter.models import Tweet
from syncr.delicious.models import Bookmark
from tagging.templatetags import tagging_tags
import re
Article = models.get_model('meowr', 'article')
Section = models.get_model('meowr', 'section')
Exit = models.get_model('meowr', 'exit')
Rating = models.get_model('meowr', 'rating')
Tag = models.get_model('tagging', 'tag')
Tweet = models.get_model('twitter', 'tweet')
Bookmark = models.get_model('delicious', 'bookmark')

register = template.Library()

class MeowrSections(template.Node):
  def __init__(self, var_name):
    self.var_name = var_name
  
  def render(self, context):
    sections = Section.objects.all()
    context[self.var_name] = sections
    return ''

@register.tag(name='get_meowr_sections')
def do_get_meowr_sections(parser, token):
  try:
    tag_name, arg = token.contents.split(None, 1)
  except ValueError:
    raise template.TemplateSyntaxError, "%s tag requires arguments" % token.contents.split()[0]
  m = re.search(r'as (\w+)', arg)
  if not m:
    raise template.TemplateSyntaxError, "%s tag had invalid arguments" % tag_name
  var_name = m.groups()[0]
  return MeowrSections(var_name)


class MeowrExits(template.Node):
  def __init__(self, var_name):
    self.var_name = var_name

  def render(self, context):
    exits = Exit.objects.all().order_by('?')[0:4]
    context[self.var_name] = exits
    return ''

@register.tag(name='get_meowr_exits')
def do_get_meowr_exits(parser, token):
  try:
    tag_name, arg = token.contents.split(None, 1)
  except ValueError:
    raise template.TemplateSyntaxError, "%s tag requires arguments" % token.contents.split()[0]
  m = re.search(r'as (\w+)', arg)
  if not m:
    raise template.TemplateSyntaxError, "%s tag had invalid arguments" % tag_name
  var_name = m.groups()[0]
  return MeowrExits(var_name)


class MeowrRatings(template.Node):
  def __init__(self, var_name):
    self.var_name = var_name

  def render(self, context):
    ratings = Rating.objects.all()
    context[self.var_name] = ratings
    return ''

@register.tag(name='get_meowr_ratings')
def do_get_meowr_ratings(parser, token):
  try:
    tag_name, arg = token.contents.split(None, 1)
  except ValueError:
    raise template.TemplateSyntaxError, "%s tag requires arguments" % token.contents.split()[0]
  m = re.search(r'as (\w+)', arg)
  if not m:
    raise template.TemplateSyntaxError, "%s tag had invalid arguments" % tag_name
  var_name = m.groups()[0]
  return MeowrRatings(var_name)


class MeowrTags(template.Node):
  def __init__(self, var_name):
    self.var_name = var_name

  def render(self, context):
    tags = Tag.objects.usage_for_model(Article, counts=True)
    context[self.var_name] = tags
    return ''

@register.tag(name='get_meowr_tags')
def do_get_meowr_tags(parser, token):
  try:
    tag_name, arg = token.contents.split(None, 1)
  except ValueError:
    raise template.TemplateSyntaxError, "%s tag requires arguments" % token.contents.split()[0]
  m = re.search(r'as (\w+)', arg)
  if not m:
    raise template.TemplateSyntaxError, "%s tag had invalid arguments" % tag_name
  var_name = m.groups()[0]
  return MeowrTags(var_name)

class MeowrTweets(template.Node):
  def __init__(self, var_name):
    self.var_name = var_name

  def render(self, context):
    tweets = Tweet.objects.all()[0:1]
    context[self.var_name] = tweets
    return ''

@register.tag(name='get_meowr_tweets')
def do_get_meowr_tweets(parser, token):
  try:
    tag_name, arg = token.contents.split(None, 1)
  except ValueError:
    raise template.TemplateSyntaxError, "%s tag requires arguments" % token.contents.split()[0]
  m = re.search(r'as (\w+)', arg)
  if not m:
    raise template.TemplateSyntaxError, "%s tag had invalid arguments" % tag_name
  var_name = m.groups()[0]
  return MeowrTweets(var_name)

class MeowrBookmarks(template.Node):
  def __init__(self, var_name):
    self.var_name = var_name

  def render(self, context):
    bookmarks = Bookmark.objects.all()[0:6]
    context[self.var_name] = bookmarks
    return ''

@register.tag(name='get_meowr_bookmarks')
def do_get_meowr_bookmarks(parser, token):
  try:
    tag_name, arg = token.contents.split(None, 1)
  except ValueError:
    raise template.TemplateSyntaxError, "%s tag requires arguments" % token.contents.split()[0]
  m = re.search(r'as (\w+)', arg)
  if not m:
    raise template.TemplateSyntaxError, "%s tag had invalid arguments" % tag_name
  var_name = m.groups()[0]
  return MeowrBookmarks(var_name)