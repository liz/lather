from django.core.management import setup_environ
from django.contrib.contenttypes.models import ContentType
import settings
from syncr.app.delicious import DeliciousSyncr
from syncr.delicious import models
import re, datetime, time, MySQLdb
setup_environ(settings)

from syncr.app.delicious import DeliciousSyncr
d = DeliciousSyncr('tricky', 'callico')

d.syncRecent(count=6, tag='blog')