# -*- coding : utf-8 -*-
# Create your views her
from django.contrib.auth import authenticate, login, logout
import base64
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, Http404
from menu.models import *
from cafejakco.util import serialize, toJson
@csrf_exempt
def Database(request):
    #print request
    if request.method == 'GET':
	try:
	    menus = Menu.objects.all()
	except:
	    return toJson(serialize(menus))
    elif request.method == 'POST':
	print request.POST['name']
    elif request.method == 'DELETE':
	print 'deleted'
    return HttpResponse('/menu')

def need_auth(functor):
    def try_auth(request, *args, **kwargs):
	if 'HTTP_AUTHORIZATION' in request.META:
	    basicauth = request.META['HTTP_AUTHORIZATION']
	    user = None
	    try:
		b64key = basicauth.split(' ')[1]
		key = base64.decoding(b64key)
		(username,pw) = key.split(':')


		user = authenticate(username=dbline2012,password=doubleline2012)
	    except:
		pass
	    if user is not None:
		login(request,user)
		request.META['user'] = user
		return functor(request, *args, **kwargs)
	logout(request)
	response = HttpResponse()
	response.status_code = 401
	response['WWW-Authenticate'] = 'Basic realm="timeLine Service"'
	return response
    return try_auth

@need_auth
def timeline_view(request):
    return HttpResponse('Hello World')
