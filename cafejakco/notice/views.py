# Create your views here
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render_to_response
from django.http import HttpResponse, Http404
from notice.models import *
from cafejakco.util import serialize, toJson
from cafejakco.auth import need_auth

@csrf_exempt
@need_auth
def NoticeResource(request, notice_id=1):
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
def NoticeDetailResource(request,notice_id=1):
	notice_id = int(notice_id)
	if request.method == 'GET':
		try:
			n = Notice.objects.get(id=notice_id)
			print n
			return toJson(serialize(n))
		except:
			raise Http404
	elif request.method == 'DELETE':
		try:
			print 'deleted'
		except:
			raise Http404
	return HttpResponse('/noticeDetailResource')

@csrf_exempt
@need_auth
def NoticeImagePost(request):
	if request.method == 'GET':
		raise Http404
	elif request.method == 'POST':
		try:
			form = Imageform(request.POST, request.FILES)
			if form.is_valid() and form.is_multipart():
				save_file(request.FILES['image'])
				return HttpResponse('Image Posted')
			else:
				return HttpResponse('Invalid Image')
		except:
			raise Http404
	else:
		 form = Imageform()
	return render_to_response('home/upload_image_form.html', {'form':form})

def save_file(file, path=' '):
	filename = file.__get_name()
	fd = open('%s/%s' %(MEDIA_ROOT, str(path) + str(filename)), 'wb')
	for chunk in file.chunks():
		fd.write(chunk)
	fd.close()
