from django.contrib.auth import authenticate, login, logout
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

		user = authenticate(username=username, password=pw)
	    except:
		pass

	    if user is not None:
		login(request, user)
		request.META['user'] = user

	    logout(request)
	    response = HttpResponse()
	    response.status_code = 401
	    response['WWW-Authenticate'] = 'Basic realm="timeLine Service"'
	    return response
	return try_auth
