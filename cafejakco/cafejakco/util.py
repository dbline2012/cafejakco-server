from django.http import HttpResponse
from django.db import models
import json

def serialize(objs):
    serialized = []
    
    if isinstance(objs, models.Model) is True:
        serialized.append(objs.serialize())
        return serialized
    
    for obj in objs:
        serialized.append(obj.serialize())
    return serialized

def toJson(objs, status=200):
    j = json.dumps(objs, ensure_ascii=False)
    return HttpResponse(j, status=status, content_type='application/json; charset=utf-8')
