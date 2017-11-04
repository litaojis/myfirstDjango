from django.shortcuts import render
from django.template.loader import render_to_string
from django.http import HttpResponse,JsonResponse
import os
import json
from django.views.generic import View
from django.views.generic.base import TemplateView
from blog.models import Article

# Create your views here.

class MyView(View):
    

    def get(self,request,*args,**kwargs):
        return HttpResponse('Hello World')


def my_view(request):
    context =   {'some_key':'some_value'}

    static_html = '/path/to/static.html'

    if not os.path.exists(static_html):
        content  = render_to_string('template.html',context)
        with open(static_html,'w') as static_file:
            static_file.write(content)

    return render(request,static_html)

def json_list(request):
    ll = list(range(100))
    print(type(ll))
    return JsonResponse(ll,safe=False)

def json_dict(request):
    dic = {'twz':'Python and Django','book':'Django fast learn'}
    return JsonResponse(dic)





