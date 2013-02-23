from external.base_views import BaseView, render_html, authorized_user_required
from blog.models import Blog, Post
from django.http import HttpResponse, HttpResponseRedirect
from blog.forms import PostForm


class BlogView(BaseView):

    @render_html('blog/list.html')
    def list_blogs(self, request, *args, **kwargs):
        return {'blogs': Blog.objects.filter(active = True)}

    @render_html('blog/index.html')
    def index(self, request, *args, **kwargs):
        entries = request.blog.get_entries()
        return { 'posts' : entries,
                 'lastcount' : entries.count() }

    @authorized_user_required('/login/')
    @render_html('blog/add.html')
    def add(self, request, *args, **kwargs):
        form = PostForm(data = request.POST if request.POST else None,
                        files = request.FILES if request.POST else None,)
        if form.is_valid():
            post = form.save(commit = False)
            post.blog = request.blog
            post.user = request.user
            post.save()
            return HttpResponseRedirect(request.blog.get_url())
        return {'post_add_form': form}
