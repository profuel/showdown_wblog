from django.conf import settings
from django.db import models

class Blog(models.Model):
	alias = models.CharField(unique = True, max_length = 32, null = False, blank = False)
	name = models.CharField(max_length = 256, default = '', null = False, blank = False)
	active = models.BooleanField(default = True)

class Post(models.Model):
	blog = models.ForeignKey(Blog)
	message = models.TextField(max_length = 1024)
	image = models.ImageField(upload_to = settings.UPLOAD_DIR)
