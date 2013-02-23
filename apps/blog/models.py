from django.conf import settings
from django.db import models
from django.contrib.auth.models import User


UPLOAD_DIR = settings.UPLOAD_DIR


class Blog(models.Model):
    alias = models.CharField(unique=True,
                             max_length=32,
                             null=False,
                             blank=False)
    name = models.CharField(max_length=256,
                            default='',
                            null=False,
                            blank=False)
    active = models.BooleanField(default=True)

    def __unicode__(self):
        return self.name

    def get_entries(self, first=0, count=settings.DEFAULT_MESSAGES_COUNT):
        return self.post_set.all().order_by('-pk')[first:count]

    def get_url(self):
        return '/blog/%s/' % self.alias


class Post(models.Model):
    blog = models.ForeignKey(Blog)
    message = models.TextField(max_length=1024)
    image = models.ImageField(upload_to=UPLOAD_DIR, null=True, blank=True)
    user = models.ForeignKey(User, blank=True, null=True)

    def __unicode__(self):
        return '%(name)s%(postfix)s' % \
                    {'name': self.message[0:20],
                     'postfix': '' if len(self.message) < 20 else '...'}
