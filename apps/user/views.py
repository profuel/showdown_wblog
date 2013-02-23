from external.base_views import BaseView, render_html
from apps.user.forms import LoginForm, RegisterForm
from django.http import HttpResponseRedirect
from django.contrib.auth import logout


class UserView(BaseView):

    @render_html('user/login.html')
    def login(self, request):
        form = LoginForm(request, data = request.POST if request.POST else None)
        if form.is_valid():
            return HttpResponseRedirect(request.GET.get('back', '/blog/'))
        return {'form': form}

    def logout(self, request):
        logout(request)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', ''))

    @render_html('user/register.html')
    def register(self, request):
        form = RegisterForm(data = request.POST if request.POST else None)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(request.GET.get('back', '/blog/'))
        return {'form': form}
