# -*- coding : utf-8 -*-
# Create your views here
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, Http404
from menu.models import *
from cafejakco.util import *
from cafejakco.auth import *
@csrf_exempt
def MenuResource(request):
    if request.method == 'GET':
	try:
	    menus = Menu.objects.all()
	    return toJson(serialize(menus))
	except:
	    pass
    elif request.method == 'POST':
	post_json_data = json.loads(request.raw_post_data)
	try:
            m = Menu(name=post_json_data['name'])
            m.save()
            return toJson({'status':'create success'})
        except:
	   pass
    elif request.method == 'DELETE':
	print 'deleted'
    return HttpResponse('Func:menuResource')
@need_auth
def timeline_view(request):
    return MenuResource(request)
