# -*- coding: utf-8 -*-
# Create your views here.
from django.http import HttpResponse, Http404
from django.contrib.auth.models import User
from community.models import *
from django.template import Context, loader
from django.views.decorators.csrf import csrf_exempt
from cafejakco.util import serialize, toJson
from cafejakco.auth import need_auth
import json
from django.core.paginator import Paginator

def index(request):
	return HttpResponse('cafejakco server')
	
# 	try:
# 		articles = Article.objects.all().order_by('-created')
# 		pages = Paginator(articles, 10)
# 		pno = 1
# 		try:
# 			if request.method == 'GET':
# 				pno = request.GET['pno']
# 				if int(pno) > pages.num_pages:
# 					return toJson([])
# 		except:
# 			pass
# 		print pages.page(pno)
# 		return toJson(serialize(pages.page(pno).object_list))
# 	except:
# 		raise Http404


def groupResource(request):
	if request.method == 'GET':
		try:
			groups = Group.objects.all()
			return toJson(serialize(groups))
		except:
			raise Http404
	elif request.method == 'POST':
		post_json_data = json.loads(request.raw_post_data)
		try:
			g = Group(name=post_json_data['name'])
			g.save()
			return toJson({'status':'create success'})
		except:
			return toJson({'status':'create fail'}, 400)
	elif request.method == 'DELETE':
		print 'DELETE method'
	return HttpResponse('Func:groupResource')


def articleResource(request, group_id=1):
	group_id = int(group_id)
		
	if request.method == 'GET':
		try:
			g = Group.objects.get(id=group_id)
			a = Article.objects.filter(group=g).order_by('-created')
				
			pages = Paginator(a, 10)
			pno = 1
			try:
				pno = request.GET['pno']
				if int(pno) > pages.num_pages:
					return toJson([])
			except:
				pass
			
			return toJson(serialize(pages.page(pno).object_list))     
		except:
			raise Http404


def articleDetailResource(request, group_id=1, article_id=1):
	group_id = int(group_id)	
	article_id = int(article_id)
	if request.method == 'GET':
		try:
			g = Group.objects.get(id=group_id)
			a = Article.objects.filter(id=article_id)
			print a
			return toJson(serialize(a)) 
		except:
			raise Http404


def articlePostResource(request):
	if request.method == 'POST':
		post_json_data = json.loads(request.raw_post_data)
		print post_json_data
		try:
			u = User.objects.get(id=int(post_json_data['user_id']))
			g = Group.objects.get(id=int(post_json_data['group_id']))
			a = Article(
						user=u,
						group=g,
						title=post_json_data['title'],
						content=post_json_data['content'],
						image=post_json_data['image'],
						)
			a.save()
			return toJson({'status':'create success'})
		except:
			return toJson({'status':'create fail'}, 400)
	else:
		raise Http404


def communityImageResource(request):
	return HttpResponse('/community/image')