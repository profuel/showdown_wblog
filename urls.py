from django.conf import settings
from django.conf.urls.defaults import patterns

from apps.blog.urls import urlpatterns as blog_patterns

urlpatterns = patterns('')

urlpatterns = blog_patterns + urlpatterns

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    )
