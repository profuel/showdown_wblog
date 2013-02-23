from external.base_views import BaseView
from django.conf import settings
from django.http import HttpResponse
from django.core import serializers


class BlogApiView(BaseView):

    def get(self, request, n_from=0, n_count=-1, *args, **kwargs):
        n_count = int(n_count)
        n_from = int(n_from)
        if n_count == -1:
            n_count = settings.DEFAULT_MESSAGES_COUNT
        n_to = n_from + n_count
        posts = request.blog.post_set.all().order_by('-pk')[n_from:n_to]
        data = serializers.serialize("json", posts)
        return HttpResponse(data)
