from external.base_views import BaseView, render_html

class BlogView(BaseView):
	@render_html('blog/index.html')
	def index(self, request):
		return {}
