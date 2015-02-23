from django.shortcuts import render, render_to_response, redirect
from django.contrib.auth.models import User
from django.core.context_processors import csrf
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login, logout
from django.template import RequestContext
from .models import Information , SkillofUser , Skill , Category
from django.contrib.auth.decorators import login_required


# Create your views here.
def mainpage(request):

	if request.user.is_authenticated():
		args={}
		if hasattr(request.user, 'information'):
			args={"user":request.user}
			return render_to_response('home/mainpage.html',args)
		else:
			return redirect(reverse('home:create_info'))
	else:
		return redirect(reverse('main:signin'))
		
def profile(request):
	if request.user.is_authenticated():
		args={}
		if hasattr(request.user, 'information'):
			args={"user":request.user}
			return render_to_response('home/profile.html',args)
		else:
			return redirect(reverse('home:create_info'))
	else:
		return redirect(reverse('main:signin'))

def create_info(request):
	args={}
	args.update(csrf(request))
	args = {'user':request.user}

	if request.POST:
		user = request.user
		image = request.POST.get('image','')
		gender = request.POST.get('gender','')
		born_date = request.POST.get('born','')
		phone_number = request.POST.get('number','') 
		address = request.POST.get('address','')
		information = Information.objects.create(user = user,image = image, gender = gender, born_date = born_date, phone_number = phone_number, address = address)
		
		information.save()
		return redirect(reverse('home:mainpage'))

	return render_to_response('home/create_info.html',args,context_instance = RequestContext(request))
@login_required(login_url=reverse('main:signin'))
def add_skill(request):
	return render_to_response('home/added.html')




