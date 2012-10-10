# Create your views here
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, Http404
from notice.models import *
from cafejakco.util import serialize, toJson
from cafejakco.auth import need_auth

@csrf_exempt
@need_auth
def NoticeResource(request):
    #print request
    if request.method == 'GET':
	try:
	    notices = Notice.objects.all()
	    return toJson(serialize(notices))
	except:
	    raise Http404 
    elif request.method == 'POST':
	post_json_data = json.load(request.raw_post_data)
	try:
	    n = Notice(name=post_json_data['name']
	    n.save()
	    return toJson({'status':'create success'})
	except:
	    pass	
    elif request.method == 'DELETE':
	print 'deleted'
    return HttpResponse('/notice')
