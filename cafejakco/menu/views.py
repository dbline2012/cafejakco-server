# -*- coding : utf-8 -*-
# Create your views here
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator
from django.http import HttpResponse, Http404
from menu.models import *
from cafejakco.util import serialize, toJson
from cafejakco.auth import need_auth

@csrf_exempt
@need_auth
def menuResource(request):
	if request.method == 'GET':
		try:
			menus = Menu.objects.all()
			return toJson(serialize(menus))
		except:
			raise Http404
	elif request.method == 'POST':
		post_json_data = json.loads(request.raw_post_data)
		try:
			m = Menu(
					name=post_json_data['name']
					)
			m.save()
			return toJson({'status':'create success'})
		except:
			return toJson({'status':'create fail'}, 400)
	elif request.method == 'DELETE':
		print 'deleted'
	return HttpResponse('Func:menuResource')

@csrf_exempt
@need_auth
def MenuList(request, menu_id=1):
	menu_id = int(menu_id)
	if request.method == 'GET':
		try:
			m = Menu.objects.get(id=menu_id)
			print m
			return toJson(serialize(m))
		except:
			raise Http404
