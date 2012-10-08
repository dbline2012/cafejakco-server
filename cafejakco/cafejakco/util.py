import json

def serialize(objs):
    serialized = []
    for obj in objs:
        serialized.append(obj.serialize())
    return serialized

def toJson(objs, status=200):
    j = json.dumps(objs, ensure_ascii=False)
    return HttpResponse(j, status=status, content_type='application/json; charset=utf-8')

