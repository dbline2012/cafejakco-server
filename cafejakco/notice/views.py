<<<<<<< HEAD
# Create your views here
import json
from django.http impprt HttpResponse, Http404
from notice.models import *

def database(request):
    if request.method == 'GET'
       notices = Notice.objects.all()
