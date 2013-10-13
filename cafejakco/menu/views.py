# -*- coding : utf-8 -*-
# Create your views here
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.http import HttpResponse, Http404
from django.template import Context, loader
from menu.models import *
from cafejakco.util import serialize, toJson
import json


def menuResource(request, menu_id=1):
	menu_id = int(menu_id)
	if request.method == 'GET':
		try:
			menus = Menu.objects.all()
			print menus
			return toJson(serialize(menus))
		except:
			raise Http404
	elif request.method == 'POST':
		post_json_data = json.loads(request,raw_post_data)
		print post_json_data
		try:
			i = Menu.objects.get(id=post_json_data['user_id'])
			m = Menu(
					id=i,
					name=post_json_data['name'],
					category=post_json_data['name'],
					desc=post_json_data['desc'],
					cost=post_json_data['cost'],
					)
			m.save()
			return toJson({'status':'create success'})
		except:
			return toJson({'status':'create fail'}, 400)
	elif request.method == 'DELETE':
		print 'deleted'
	return HttpResponse('Func:menuResource')


def menuDetailResource(request, menu_id=1):
	menu_id = int(menu_id)
	if request.method == 'GET':
		try:
			m = Menu.objects.filter(id=menu_id)
			print m
			return toJson(serialize(m))
		except:
			raise Http404
	elif request.method == 'PUT':
		pass
	elif request.method == 'DELETE':
		print 'deleted'
	return HttpResponse('Func:menuDetailResource')	
