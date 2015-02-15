from django.shortcuts import render, render_to_response
from django.contrib.auth.models import User
from django.core.context_processors import csrf
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login, logout
from django.template import RequestContext


def mainpage(request):
	return render_to_response('main/mainpage.html',{},context_instance = RequestContext(request))

def signin(request):
	args={}
	args.update(csrf(request))
	if request.POST:
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		if user is not None:
			if user.is_active:
				login(request, user)
				args = {'user':user}
				return render_to_response('main/thanks.html',args)
			else:
				return render_to_response('main/signup.html',args)
		else:
			return render_to_response('main/signup.html',args)
	else:
		return render_to_response('main/signin.html',args)

def signout(request):
    logout(request)
    return render_to_response('main/mainpage.html',{},context_instance = RequestContext(request))


def signup(request):
	args={}
	args.update(csrf(request))
	if request.POST:
		first_name = request.POST.get('firstname','')
		last_name = request.POST.get('lastname','')
		username = request.POST.get('username','')
		password = request.POST.get('password','')
		password1 = request.POST.get('password1','')
		email = request.POST.get('email','')



		if password1 == password:
			user = User.objects.create_user(username, email, password)
			user.first_name = first_name
			user.last_name = last_name
			user.save()
			return render_to_response('main/signin.html',args)
		else:
			return render_to_response('main/signup.html',args)

		


	else:
		return render_to_response('main/signup.html',args)

	


