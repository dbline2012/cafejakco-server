# -*- coding: utf-8 -*-

# Create your views here.
from django.http import HttpResponse, Http404
from django.contrib.auth.models import User
from community.models import *
from django.template import Context, loader
from django.views.decorators.csrf import csrf_exempt
from cafejakco.util import serialize, toJson
import json

def index(request):
    articles = Article.objects.all()
    print articles
    return toJson(serialize(articles))

@csrf_exempt
def groupResource(request):
    #print request
    if request.method == 'GET':
        groups = Group.objects.all()
        print groups
        return toJson(serialize(groups)) 
       
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
        
    return HttpResponse('/coumunity')

@csrf_exempt
def articleResource(request, group_id=1):
    group_id = int(group_id)
    if request.method == 'GET':
        try:
            g = Group.objects.get(id=group_id)
            a = Article.objects.filter(group=g)
            return toJson(serialize(a))        
        except:
            return HttpResponse('존재하지않습니다.')
        
    elif request.method == 'POST':
        post_json_data = json.loads(request.raw_post_data)
        print post_json_data
        try:
            u = User.objects.get(id=post_json_data['user_id'])
            g = Group.objects.get(id=group_id)
            a = Article(
                        user=u,
                        group=g,
                        title=post_json_data['title'],
                        content=post_json_data['content'],
                        image=post_json_data['image']
                        )
            a.save()
            return toJson({'status':'create success'})
        except:
            return toJson({'status':'create fail'}, 400)
 
@csrf_exempt       
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
            return HttpResponse('존재하지않습니다.')


@csrf_exempt
def communityImageResource(request):
    return HttpResponse('/community/image')