# -*- coding: utf-8 -*-

# Create your views here.
from django.http import HttpResponse, Http404
from django.contrib.auth.models import User
from community.models import Group
from membership.models import *
from django.views.decorators.csrf import csrf_exempt
from cafejakco.util import serialize, toJson
from django.contrib.auth import authenticate, login, logout
import json

@csrf_exempt
def memberResource(request):
    if request.method == 'GET':
        members = Member.objects.all()
        return toJson(serialize(members))
    
    elif request.method == 'POST':
        post_json_data = json.loads(request.raw_post_data)
        print 'memberResource : ', post_json_data
        try:
            u = User.objects.create_user(
                                         username=post_json_data['username'],
                                         password=post_json_data['password'],
                                         email=post_json_data['username']
                                         )
            u = User.objects.get(username=post_json_data['username'])
            g = Group.objects.get(id=3)
            
            
            m = Member(
                       user=u,
                       group=g,
                       nickname=post_json_data['nickname'],
                       image=post_json_data['image'],
                       sex=post_json_data['sex']
                       )
            m.save()
            return toJson([{'status':'success', "message":"member joined success"}])
        except:
            return toJson([{'status':'fail', "message":"member joined fail"}])

@csrf_exempt
def memberDetailResource(request, user_id=1):
    user_id = int(user_id)  
    if request.method == 'GET':
        try:
            u = User.objects.get(id=user_id)
            m = Member.objects.filter(user=u)
            return toJson(serialize(m))
        except:
            raise Http404
        
        
def couponResource(request):
    if request.method == 'GET':
        try:
            coupons = Coupon.objects.all()
            return toJson(serialize(coupons))
        except:
            raise Http404
    elif request.method == 'POST':
        post_json_data = json.loads(request.raw_post_data)
        
        try:
            c = Coupon(
                       title=post_json_data['title'],
                       content=post_json_data['content'],
                       end=post_json_data['end'],
                       )
            c.save()  
            return toJson([{'status':'create success'}])
        except:
            return toJson([{'status':'create fail'}], 400)
      
def couponDetailResource(request, coupon_id=1):
    coupon_id = int(coupon_id)    
    if request.method == 'GET':
        try:
            c = Coupon.objects.filter(id=coupon_id)
            return toJson(serialize(c))
        except:
            raise Http404
        
@csrf_exempt
def login(request):
    if request.method == 'POST':
        post_json_data = json.loads(request.raw_post_data)
        
        try:
            username=post_json_data['username']
            password=post_json_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    m = Member.objects.get(user=user)
                    print '[login] user is logined : %s' % (m)
                    return toJson(serialize(m))
        except:
            return toJson([{'status':'fail', 'message':'login fail'}])
            
        return toJson([{'status':'fail', 'message':'login fail'}])


def logout(request):
    try:
        logout(request)
    except:
        return toJson({'status':'logout fail'})
    return toJson({'status':'logout success'})