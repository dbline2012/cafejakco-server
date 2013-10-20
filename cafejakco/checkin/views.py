# -*- coding: utf-8 -*-

# Create your views here.
from django.http import HttpResponse, Http404
from django.contrib.auth.models import User
from checkin.models import *
from django.views.decorators.csrf import csrf_exempt
from cafejakco.util import serialize, toJson
import json


def checkinResource(request):
    if request.method == 'GET':
        try:
            checkins = Checkin.objects.all()
            return toJson(serialize(checkins))
        except:
            return Http404
        
    elif request.method == 'POST':
        post_json_data = json.loads(request.raw_post_data)
        
        try:
            u = User.objects.get(id=post_json_data['user_id'])
            
            ch = Checkin(
                         user=u,
                         )
            ch.save()
            return toJson([{'status':'success', 'message':'checkin success'}])
        except:
            return toJson([{'status':'fail'}], 400)


def userCheckinResource(request, user_id=1):
    user_id = int(user_id)
    
    if request.method == 'GET':
        try:
            u = User.objects.get(id=user_id)
            ch = Checkin.objects.filter(user=u)
            return toJson(serialize(ch))
        except:
            raise Http404
