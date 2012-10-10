# -*- coding : utf-8 -*-
# Create your views her
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, Http404
from menu.models import *
from cafejakco.util import serialize, toJson
from cafejakco.m_auth import need_auth
@csrf_exempt
def Database(request):
    #print request
    if request.method == 'GET':
	try:
	    menus = Menu.objects.all()
	    return toJson(serialize(menus))
	except:
	    pass
    elif request.method == 'POST':
	print request.POST['name']
    elif request.method == 'DELETE':
	print 'deleted'
    return HttpResponse('/menu')

@csrf_exempt
@need_auth
def timeline_view(request):
    return HttpResponse('Hello World!')
