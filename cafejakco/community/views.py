# -*- coding: utf-8 -*-

# Create your views here.
from django.http import HttpResponse, Http404
from community.models import *
from django.template import Context, loader
from django.views.decorators.csrf import csrf_exempt



def index(request):
    articles = Article.objects.all()
    print articles
    if request.method == 'POST':
        print 'ppppppp'
    
    try:
        g = Group(name='작커')
        g.save()
        print g.id
        return HttpResponse('작커 입력완료')
        
    except:
        return HttpResponse('이미 존재하는 그룹 이름입니다.')

@csrf_exempt
def communityService(request):
    print request
    if request.method == 'GET':
        groups = Group.objects.all()
        print groups, ' Get method'
        
    elif request.method == 'POST':
        print 'POST method'
        
    elif request.method == 'DELETE':
        print 'DELETE method'
        
    return HttpResponse('/coumunity')

def communityServiceDetail(request, group_id=1):
    group_id = int(group_id)
    if request.method == 'GET':
        try:
            groups = Group.objects.get(id=group_id)
        except:
            return HttpResponse('존재하지않습니다.')
    return HttpResponse(groups)

