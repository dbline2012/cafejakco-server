# -*- coding: utf-8 -*-

# Create your views here.
from django.http import HttpResponse, Http404
from django.contrib.auth.models import User
from community.models import Group
from membership.models import *
from django.views.decorators.csrf import csrf_exempt
from cafejakco.util import serialize, toJson
import json

@csrf_exempt
def memberResource(request):
    if request.method == 'GET':
        members = Member.objects.all()
        return toJson(serialize(members))
    
    elif request.method == 'POST':
        post_json_data = json.loads(request.raw_post_data)
        
        try:
            u = User.objects.create_user(
                                         username=post_json_data['username'],
                                         email=post_json_data['email'],
                                         password=post_json_data['password'],
                                         )
            u = User.objects.get(username=post_json_data['username'])
            g = Group.objects.get(id=1)
            m = Member(
                       user=u,
                       group=g,
                       nickname=post_json_data['nickname'],
                       sex=post_json_data['sex'],
                       image=post_json_data['image'],
                       )
            m.save()
            return toJson({'status':'create success'})
        except:
            return toJson({'status':'create fail'}, 400)
  
@csrf_exempt
def memberDetailResource(request, user_id=1):
    user_id = int(user_id)
    
    if request.method == 'GET':
        u = User.objects.get(id=user_id)
        m = Member.objects.filter(user=u)
        return toJson(serialize(m))
        
@csrf_exempt      
def couponResource(request):
    if request.method == 'GET':
        coupons = Coupon.objects.all()
        return toJson(serialize(coupons))
    
    elif request.method == 'POST':
        post_json_data = json.loads(request.raw_post_data)
        
        try:
            c = Coupon(
                       title=post_json_data['title'],
                       content=post_json_data['content'],
                       end=post_json_data['end'],
                       )
            c.save()  
            return toJson({'status':'create success'})
        except:
            return toJson({'status':'create fail'}, 400)