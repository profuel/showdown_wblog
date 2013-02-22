from django.conf.urls.defaults import patterns, url
from apps.blog.views import BlogView
from blog.views_api import BlogApiView

blog_view = BlogView()
blog_api_view = BlogApiView()

urlpatterns = patterns('',
                    url(r'^blog/$', blog_view, {'action' : 'list_blogs'}),
                    url(r'blog/(?P<blogname>.+)/', blog_view, {'action' : 'index'}),
                    url(r'blog/(?P<blogname>.+)/add/$', blog_view, {'action' : 'add'}),
                    url(r'blog/(?P<blogname>.+)/get/(?P<from>\d+)/$', blog_view, {'action' : 'get'}),
                    url(r'blog/(?P<blogname>.+)/get/(?P<from>\d+)/(?P<to>\d+)/$', blog_api_view, {'action' : 'get'}),
)
