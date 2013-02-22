from django.conf import settings
from django.conf.urls.defaults import patterns, include

from apps.blog.urls import urlpatterns as blog_patterns

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
        (r'^admin/', include(admin.site.urls)),
)

urlpatterns = blog_patterns + urlpatterns

urlpatterns += patterns('',
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
)
