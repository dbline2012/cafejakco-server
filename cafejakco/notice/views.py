# Create your views here
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render_to_response
from django.http import HttpResponse, Http404
from notice.models import *
from cafejakco.util import serialize, toJson
from cafejakco.auth import need_auth

@csrf_exempt
def noticeResource(request, notice_id=1):
	notice_id = int(notice_id)
	#print request
	if request.method == 'GET':
		try:
			notices = Notice.objects.all()
			return toJson(serialize(notices))
		except:
			raise Http404 
	elif request.method == 'POST':
		post_json_data = json.loads(request.raw_post_data)
		try: 
			n = Notice(
						title=post_json_data['title'],
						content=post_json_data['content'],
						created=post_json_data['created'],
					  )
			n.save()
			return toJson({'status':'create success'})
		except:
			return toJson({'status':'create fail'})
	elif request.method == 'DELETE':
		print 'deleted'
	return HttpResponse('/notice')

@csrf_exempt
@need_auth
def noticeDetailResource(request, notice_id=1):
	notice_id = int(notice_id)
	if request.method == 'GET':
		try:
			n = Notice.objects.get(id=notice_id)
			print n
			return toJson(serialize(n))
		except:
			raise Http404
	elif request.method == 'POST':
		post_json_data = json.loads(request.raw_post_data)
		try:
			n = Notice(
						image=post_json_data['image'],
					  )
			n.save()
			return toJson({'status':'create success'})
		except:
			return toJson({'status':'create fail'})
	elif request.method == 'DELETE':
		try:
			print 'deleted'
		except:
			raise Http404
	return HttpResponse('/noticeDetailResource')
