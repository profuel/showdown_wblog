from django.conf.urls.defaults import patterns, url
from apps.blog.views import BlogView

blog_view = BlogView()

urlpatterns = patterns('',
					url(r'', blog_view, {'action' : 'index'}),
)
