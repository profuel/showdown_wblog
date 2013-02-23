from apps.blog.models import Blog
from django.http import Http404

class BlogMiddleware(object):

    def process_request(self, request):
        try:
            parts = request.META['PATH_INFO'].rstrip('/').split('/')
            if parts[1] in ['media', 'user', 'admin']:
                return
            alias = parts[2]
            if alias == 'admin':
                return
            request.blog = Blog.objects.get(alias = alias)
        except Blog.DoesNotExist:
            raise Http404
        except IndexError:
            pass
        return None
