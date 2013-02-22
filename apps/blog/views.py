from external.base_views import BaseView, render_html

class BlogView(BaseView):

    @render_html('blog/index.html')
    def index(self, request, *args, **kwargs):
        return {'posts' : request.blog.get_entries() }

    @render_html('blog/index.html')
    def add(self, request, *args, **kwargs):
        return {}


