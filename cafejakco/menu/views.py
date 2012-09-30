# -*- coding : utf-8 -*-
# Create your views here
import json
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, Http404
from menu.models import *
@csrf_exempt

def Database(request):
    #print request
    if request.method == 'GET':
       menus = Menu.objects.all()
       return toJson(serialize(menus))
    return HttpResponse('/menu')

def serialize(objs):
    serialized = {}
    for obj in objs:
        serialized.append(obj.serialize())
    return serialized

def toJson(objs, status=200):
    j = json.dumps(objs, ensure_ascii=False)
    return HttpResponse(j, status=status, content_type='application/json; charset=utf-8')
