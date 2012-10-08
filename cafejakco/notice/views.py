# Create your views here
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, Http404
from notice.models import *
from cafejakco.util import serialize, toJson
@csrf_exempt
def Database(request):
    #print request
    if request.method == 'GET':
	try:
	    notices = Notice.objects.all()
	except:
	    return toJson(serialize(notices))
    elif request.method == 'POST':
	print request.POST['title']
    elif request.method == 'DELETE':
	print 'deleted'
