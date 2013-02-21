import json

from django.http import Http404, HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from functools import update_wrapper

class BaseView(object):
    def __call__(self, request = '', action = '', *args, **kwargs):
        if not (request):   #django 1.3 calls callable classes in templates right away
            return self
        view = getattr(self, action, None)
        if not view:
            raise Http404
        return view(request, *args, **kwargs)

def render_html(template = None, attr = None):
    def wrap(view_func):
        def wrapped_f(self, request, *args, **kwargs):
            norender = kwargs.get('_no_render', False)
            if norender:
                del kwargs['_no_render']
            context = view_func(self, request, *args, **kwargs)
            if not (isinstance(context, HttpResponse) or norender):
                context['view_obj'] = self
                if attr:
                    return render_to_response(getattr(self, attr, template), RequestContext(request, context))
                else:
                    return render_to_response(template, RequestContext(request, context))
            else:
                return context
        update_wrapper(wrapped_f, view_func)
        return wrapped_f
    return wrap

def render_json(view_func):
    def wrapped_f(self, request, *args, **kwargs):
            context = view_func(self, request, *args, **kwargs)
            if not isinstance(context, HttpResponse):
                return HttpResponse(json.dumps(context), mimetype = 'application/json')
            else:
                return context
    update_wrapper(wrapped_f, view_func)
    return wrapped_f
