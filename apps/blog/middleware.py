from apps.blog.models import Blog
from django.http import Http404

class BlogMiddleware(object):

    def process_request(self, request):
        try:
            alias = request.META['PATH_INFO'].split('/')[2]
            if alias == 'admin':
                return
            request.blog = Blog.objects.get(alias = alias)
        except (Blog.DoesNotExist, AttributeError):
            raise Http404
        return None
