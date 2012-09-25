# -*- coding: utf-8 -*-
# Create your views here.
from django.http import HttpResponse, Http404
from notice.models import *
from django.template import Context, loader
from django.views.decorators.csrf import csrf_exempt

def index(request):
    notices = Notice.objects.all()
    print notices
    if request.method == 'POST':
        print 'POSTING'
    
    try:
        n = Menu(name='공지사항')
        n.save()
        print n.id
        return HttpResponse('공지사항 입력완료')
        
    except:
        return HttpResponse('이미 존재하는 메뉴 이름입니다.')

@csrf_exempt
def noticeservice(request):
    print request
    if request.method == 'GET':
        menus = Menu.objects.all()
        print menus, ' Get method'
        
    elif request.method == 'POST':
        print 'POST method'
        
    elif request.method == 'DELETE':
        print 'DELETE method'
        
    return HttpResponse('/notice')
