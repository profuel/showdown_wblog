from django.conf import settings
from django.db import models

class Blog(models.Model):
    alias = models.CharField(unique = True, max_length = 32, null = False, blank = False)
    name = models.CharField(max_length = 256, default = '', null = False, blank = False)
    active = models.BooleanField(default = True)

    def __unicode__(self):
        return self.name

    def get_entries(self, first = 0, count = settings.DEFAULT_MESSAGES_COUNT):
        return self.post_set.all().order_by('-pk')[first:count]

class Post(models.Model):
    blog = models.ForeignKey(Blog)
    message = models.TextField(max_length = 1024)
    image = models.ImageField(upload_to = settings.UPLOAD_DIR, null = True, blank = True)

    def __unicode__(self):
        return '%(name)s%(postfix)s' % {'name': self.message[0:20], 'postfix':'' if len(self.message) < 20 else '...'}

