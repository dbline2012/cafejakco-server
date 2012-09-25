# -*- coding: utf-8 -*-
# Create your views here.
from django.http import HttpResponse, Http404
from menu.models import *
from django.template import Context, loader
from django.views.decorators.csrf import csrf_exempt

def index(request):
    menus = Menu.objects.all()
    print menus
    if request.method == 'POST':
        print 'POSTING'
    
    try:
        m = Menu(name='아메리카노')
        m.save()
        print m.id
        return HttpResponse('메뉴 입력완료')
        
    except:
        return HttpResponse('이미 존재하는 메뉴 이름입니다.')

@csrf_exempt
def menuservice(request):
    print request
    if request.method == 'GET':
        menus = Menu.objects.all()
        print menus, ' Get method'
        
    elif request.method == 'POST':
        print 'POST method'
        
    elif request.method == 'DELETE':
        print 'DELETE method'
        
    return HttpResponse('/menu')
