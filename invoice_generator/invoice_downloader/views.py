from django.shortcuts import render
from django.http.response import HttpResponse
from django.template.loader import select_template
from django.core.files.storage import FileSystemStorage

# Create your views here.


def index(request):

    if request.method == 'GET':
        template = select_template(['index.html'])
        context = {
        }

        return HttpResponse(template.render(context, request))


def nueva(request):
    
    if request.method == 'GET':
        template = select_template(['nueva.html'])
       
        context = {
        }
    
    if request.method == 'POST' and request.FILES['document']:
        document = request.FILES['document']
        fs = FileSystemStorage()
        filename = fs.save(document.name, document)
        uploaded_file_url = fs.url(filename)
        return render(request, 'nueva.html', {
            'uploaded_file_url': uploaded_file_url
        })
        # print(uploaded_file.name)
        # print(uploaded_file.size)

    return HttpResponse(template.render(context, request))

        