from external.base_views import BaseView, render_html, authorized_user_required
from blog.models import Blog
from django.http import HttpResponse


class BlogView(BaseView):

    @render_html('blog/list.html')
    def list_blogs(self, request, *args, **kwargs):
        return {'blogs' : Blog.objects.filter(active = True) }

    @render_html('blog/index.html')
    def index(self, request, *args, **kwargs):
        return { 'posts' : request.blog.get_entries() }

    @authorized_user_required('/login/')
    def add(self, request, *args, **kwargs):
        return HttpResponse('1')


