from django.core.management import setup_environ
from django.contrib.contenttypes.models import ContentType
import settings
from syncr.app.tweet import TwitterSyncr
from syncr.twitter import models
import re, datetime, time, MySQLdb
setup_environ(settings)

from syncr.app.tweet import TwitterSyncr
t = TwitterSyncr('misstricky', 'callico')

t.syncTwitterUserTweets('misstricky')