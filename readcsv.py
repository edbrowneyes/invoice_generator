import csv
import pdfkit
import urllib.parse
import os
import logging

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s.%(msecs)03d %(name)s %(levelname)s %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
path = "/Users/csozac/Downloads/reporte_44791449"
try:
    os.mkdir(path)
except OSError:
    logging.exception("Creation of the directory %s failed" % path)

with open('reporte_44791449.csv', newline='') as csvfile:
    invoiceReader = csv.reader(csvfile, delimiter=';')
    # se salta la primera linea de headers
    next(invoiceReader)
    for row in invoiceReader:
        logging.info(row[4]+" "+row[5]+" "+row[6]+" " +
                     row[7]+" "+urllib.parse.quote(row[13]))
        admPath = path+"/"+row[5]
        if not os.path.isdir(admPath):
            try:
                os.mkdir(admPath)
            except OSError:
                logging.exception("Creation of the directory %s failed" % path)
        # genera PDF a partir de la URL de la factura
        pdfkit.from_url('http://lvaindices1903.acepta.com/ca4webv3/HtmlView?url=' +
                        urllib.parse.quote(row[19]), admPath+"/"+row[2]+'.pdf')
