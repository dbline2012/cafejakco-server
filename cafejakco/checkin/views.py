# -*- coding: utf-8 -*-

# Create your views here.
from django.http import HttpResponse, Http404
from django.contrib.auth.models import User
from checkin.models import *
from django.views.decorators.csrf import csrf_exempt
from cafejakco.util import serialize, toJson
import json

@csrf_exempt
def userCheckinResource(request, user_id=1):
    user_id = int(user_id)
    
    if request.method == 'GET':
        try:
            u = User.objects.get(id=user_id)
            checkins = Checkin.objects.filter(user=u)
            return toJson(serialize(checkins))
        except:
            return HttpResponse('존재하지않습니다.')
        
    