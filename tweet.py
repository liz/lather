from django.core.management import setup_environ
from django.contrib.contenttypes.models import ContentType
import settings
from syncr.app.tweet import TwitterSyncr
from syncr.twitter import models
import re, datetime, time, MySQLdb
setup_environ(settings)
from django.conf import settings

from syncr.app.tweet import TwitterSyncr
t = TwitterSyncr(settings.TWITTER_USER, settings.TWITTER_PASS)

t.syncTwitterUserTweets(settings.TWITTER_USER)