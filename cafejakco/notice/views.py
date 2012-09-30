# Create your views here
import json
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, Http404
from notice.models import *
@csrf_exempt
def Database(request):
    #print request
    if request.method == 'GET':
       notices = Notice.objects.all()
       return toJson(serialize(notices))
    elif request.method == 'POST':
       print request.POST['title']
    elif request.method == 'DELETE':
       print 'deleted'
    return HttpResponse('/notice')

def serialize(objs):
    serialized = []
    for obj in objs:
        serialized.append(obj.serialize())
    return serialized

def toJson(objs, status=200):
    j = json.dumps(objs, ensure_ascii=False)
    return HttpResponse(j, status=status, content_type='application/json; charset=utf-8')

