from django.shortcuts import render
from django.http.response import HttpResponse
from django.template.loader import select_template

# Create your views here.


def index(request):

    if request.method == 'GET':
        template = select_template(['index.html'])
        context = {
        }

        return HttpResponse(template.render(context, request))


def test2(request):
    
    if request.method == 'GET':
        template = select_template(['test2.html'])
        context = {
        }

        return HttpResponse(template.render(context, request))