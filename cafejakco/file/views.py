# -*- coding: utf-8 -*-
# Create your views here.
from cafejakco.util import toJson
from django.views.decorators.csrf import csrf_exempt
from file.models import UploadFileForm
from cafejakco import settings
import logging


logger = logging.getLogger(__name__)


def FileHandler(request):
    if request.method == 'POST':
        if 'file' in request.FILES:
            file = request.FILES['file']
            filename = file._name
            dirname = settings.STATICFILES_DIRS[0]
            #logger.debug(filename + ' upload')
            fp = open('%s\\%s' % (dirname, filename), 'wb')
            for chunk in file.chunks():
                fp.write(chunk)
            fp.close()
            return toJson({'status':'success'})
    return toJson({'status':'fail'})


def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.FILES)
        print form.is_valid()
        if form.is_valid():
            print 'valid'
            HandleUploadedFile(request.FILES['file'])
            return toJson({'status':'success'})
    else:
        form = UploadFileForm()
    return toJson({'status':'fail'})

def HandleUploadedFile(f):
    filename = f._name
    with open('%s\\%s' % ('D:\\file', filename), 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
