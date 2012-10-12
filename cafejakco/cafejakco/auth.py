from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
import base64

def need_auth(functor):
    def try_auth(request, *args, **kwargs):
		if 'HTTP_AUTHORIZATION' in request.META:
			basicauth = request.META['HTTP_AUTHORIZATION']
			user = None
	    	try:
				b64key = basicauth.split(' ')[1]
				key = base64.decodestring(b64key)
				(username,pw) = key.split(':')

				user = authenticate(username="dbline2012", password="doubleline2012")
	    	except:
				pass

	    	if user is not None:
				login(request, user)
				request.META['user'] = user
				return functor(request, *args, **kwargs)

		logout(request)
		response = HttpResponse("Test")
		response.status_code = 401
		response['WWW-Authenticate'] = 'Basic realm="Resource Service"'
		return response
    return try_auth
