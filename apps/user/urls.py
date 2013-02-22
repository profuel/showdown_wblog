from django.conf.urls.defaults import patterns, url
from apps.user.views import UserView

user_view = UserView()

urlpatterns = patterns('',
                       url(r'user/(?P<action>\w+)/$', user_view,),
                       )
