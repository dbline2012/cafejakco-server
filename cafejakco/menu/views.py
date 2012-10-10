# -*- coding : utf-8 -*-
# Create your views here
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.http import HttpResponse, Http404
from menu.models import *
from cafejakco.util import serialize, toJson
from cafejakco.auth import *
import json
def MenuResource(request):
    if request.method == 'GET':
	try:
	    menus = Menu.objects.all()
	    return toJson(serialize(menu))
	except:
	    raise Http404
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
def need_auth(functor):
    if 'HTTP_AUTHORIZATION' in request.META:
	auth =request.META['HTTP_AUTHORIZATION']
	key = base64.decodestring(auth.split(' ')[1])
	id,pw = key.split(':')
	if id == 'dbline2012' and pw == 'doubleline2012':
	    return HttpResponse( 'Hello id: %s, pwd : %s' % (id,pw) )

	response = HttpResponse()
	response.status_code = 401
	response['WWW-Authenticate'] = 'Basic realm="Menu Resource"'
	return response

