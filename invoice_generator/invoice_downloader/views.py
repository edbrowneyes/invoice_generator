from django.shortcuts import render
from django.http.response import HttpResponse
from django.template.loader import select_template
from django.core.files.storage import FileSystemStorage
import csv
import pdfkit
import urllib.parse
import os
import logging
import shutil


# Create your views here.

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s.%(msecs)03d %(name)s %(levelname)s %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

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
        filename = fs.save(document.name, document) #NOMBRE ARCHIVO
        fs.url(filename)
       

        origin_file_path = "./media/"
        try:
            os.mkdir(origin_file_path)
        except OSError:
            logging.exception("Creation of the directory %s failed" % origin_file_path)


        target_dir_path = "./media/"+filename.replace('.csv','')
        try:
            os.mkdir(target_dir_path)
        except OSError:
            logging.exception("Creation of the directory %s failed" % target_dir_path)


        with open(origin_file_path + filename, newline='') as csvfile:
            invoiceReader = csv.reader(csvfile, delimiter=';')
            # se salta la primera linea de headers
            next(invoiceReader)
            for row in invoiceReader:
                logging.info(row[4]+" "+row[5]+" "+row[6]+" " +
                            row[7]+" "+urllib.parse.quote(row[13]))
                admPath = target_dir_path+"/"+row[5]
                if not os.path.isdir(admPath):
                    try:
                        os.mkdir(admPath)
                    except OSError:
                        logging.exception("Creation of the directory %s failed" % admPath)
                # genera PDF a partir de la URL de la factura
                pdfkit.from_url('http://lvaindices1903.acepta.com/ca4webv3/HtmlView?url=' +
                                urllib.parse.quote(row[19]), admPath+"/"+row[2]+'.pdf')
        
        shutil.make_archive(target_dir_path, 'zip', target_dir_path)
        return render(request, 'nueva.html', {
            'uploaded_file_url': target_dir_path + ".zip"
        })

    return HttpResponse(template.render(context, request))
