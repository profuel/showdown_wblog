from external.base_views import BaseView
from django.conf import settings
from django.http import HttpResponse
from django.core import serializers

class BlogApiView(BaseView):

    def get(self, request, n_from = 0, n_count = -1, *args, **kwargs):
        n_count = int(n_count)
        n_from = int(n_from)
        if n_count == -1:
            n_count = settings.DEFAULT_MESSAGES_COUNT
        data = serializers.serialize("json", request.blog.post_set.all().order_by('-pk')[n_from:n_from + n_count])
        return HttpResponse(data)
