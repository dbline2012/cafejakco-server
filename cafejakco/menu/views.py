# -*- coding : utf-8 -*-
# Create your viewawq her
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, Http404
from cafejakco.util import *
from cafejakco.m_auth import *
@csrf_exempt
def MenuResource(request):
    if request.method == 'GET':
	try:
	    menus = Menu.objects.all()
	    return toJson(serialize(menu))
	except:
	    pass
    elif request.method == 'POST':
	post_json_data = json.loads(request.raw_post_data)
	try:
            m = Menu(name=post_json_data['name'])
            m.save()
            return toJson({'status':'create success'})
        except:
            return toJson({'status':'create fail'}, 400)
    elif request.method == 'DELETE':
	print 'deleted'
    return HttpResponse('Func:menuResource')
@need_auth
def timeline_view(request):
    return MenuResource(request)
