from external.base_views import BaseView, render_json

class BlogApiView(BaseView):

    @render_json
    def get(self, request):
        return {}
