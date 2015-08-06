#python importings
from random import randint
#importings
from django.http import Http404
from django.core.paginator import Paginator
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.core.context_processors import csrf
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login, logout
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Information , SkillofUser , Skill , Category , Job, Slogan,Order
import requests


# Views
# @login_required(login_url=reverse('main:signin'))
def mainpage(request):
	#initialize variables
	args={}
	slogans = Slogan.objects.all()
	args.update(csrf(request))
	message = "JB:"
	#if user have complated registration
	#if hasattr(request.user, 'information'):

	if request.POST:
		name = request.POST.get('name', '')
		telephone = request.POST.get('telephone', '')
		category = request.POST.get('category', '')
		date_of_order = request.POST.get('date_order', '')
		job_description = request.POST.get('description', '')
		address = request.POST.get('address', '')

		category = get_object_or_404(Category, pk=category)
		new_order = Order.objects.create(name = name, job_description = job_description, telephone = telephone, category = category, date_of_order = date_of_order, address=address)
		new_order.save()
		# dealing with sms
		args["success_message"] = "ваша заявка принята , наши операторы свяжутся с вами в течении 5 минут"
		message += '\nname:' + str(name.encode('utf-8')) + '\n telephone:' + str(telephone.encode('utf-8')) + '\n date:' + str(date_of_order.encode('utf-8'))
		sms_url = 'http://smsc.ru/sys/send.php?login=traktorist221&psw=smsc120701&phones=996556606737&mes='
		sms_url += message
		r = requests.get(sms_url)
		

	# the method is get
	args['categories'] = Category.objects.all()
	args['slogan'] = slogans[0]
	return render_to_response('home/main.html',args)

def add_task(request):
	#initialize variables
	args={}
	slogans = Slogan.objects.all()
	args.update(csrf(request))

	args['categories'] = Category.objects.all()
	args['slogan'] = slogans[0]

	return render_to_response('home/add_job.html',args)
	
	
"""
@login_required(login_url=reverse('main:signin'))
def profile(request):
	#init variables
	args={}
	slogans = Slogan.objects.all()
	#if user have complated registration
	if hasattr(request.user, 'information'):
		args['user'] = request.user
		args['slogan'] = slogans[randint(0,slogans.count()-1)]
		return render_to_response('home/profile.html',args)
	else:
		return redirect(reverse('home:create_info'))
"""
"""
@login_required(login_url=reverse('main:signin'))
def create_info(request):
	#initialize variables
	args={}
	slogans = Slogan.objects.all()
	args.update(csrf(request))
	#if user have complated registration
	if hasattr(request.user, 'information'):
		return redirect(reverse('home:mainpage'))
	if request.POST:
		user = request.user
		image = request.POST.get('image','')
		gender = request.POST.get('gender','')
		born_date = request.POST.get('born','')
		phone_number = request.POST.get('number','')
		category_id = request.POST.get('category','')
		category = Category.objects.get(pk=category_id)
		note = request.POST.get('note','')
		information = Information.objects.create(user = user,image = image, gender = gender, category = category, born_date = born_date, phone_number = phone_number, note=note)
		information.save()
		return redirect(reverse('home:mainpage'))
	else:
		categories = Category.objects.all()
		args['categories'] = categories
		args['user'] = request.user
		args['slogan'] = slogans[randint(0,slogans.count()-1)]

		return render_to_response('home/create_info.html',args)
"""
"""
@login_required(login_url=reverse('main:signin'))
def modify_info(request):
	#initialize variables
	args={}
	slogans = Slogan.objects.all()
	args.update(csrf(request))

	if request.POST:
		user = request.user
		first_name = request.POST.get('firstname','')
		last_name = request.POST.get('lastname','')
		email = request.POST.get('email','')
		image = request.POST.get('image','')
		gender = request.POST.get('gender','')
		born_date = request.POST.get('born','')
		phone_number = request.POST.get('number','')
		address = request.POST.get('address','')
		note = request.POST.get('note','')

		if first_name:
			user.first_name = first_name
		if last_name:
			user.last_name = last_name
		if email:
			user.email = email
		if image:
			user.information.image = image
		if gender:
			user.information.gender = gender
		if born_date:
			user.information.born_date = born_date
		if phone_number:
			user.information.phone_number = phone_number
		if address:
			user.information.address = address
		if note:
			user.information.note = note
		user.information.save()
		user.save()
		args['user'] = request.user
		args['slogan'] = slogans[randint(0,slogans.count()-1)]
		args['success_message'] = 'Профиль успешно отредактирован'
		return render_to_response('home/profile.html',args)
	else:
		#if user have complated registration
		if hasattr(request.user, 'information'):
			args["user"] = request.user
			args['slogan'] = slogans[randint(0,slogans.count()-1)]
			return render_to_response('home/modify_info.html',args)
		else:
			return redirect(reverse('home:create_info'))

@login_required(login_url=reverse('main:signin'))
def change_password(request):
	#init variables
	args = {}
	args.update(csrf(request))
	slogans = Slogan.objects.all()
	user = request.user
	args['user'] = user
	args['slogan'] = slogans[randint(0,slogans.count()-1)]

	if request.POST:
		password1 = request.POST.get('password1','')
		password2 = request.POST.get('password2','')

		if len(password1) < 6 or len(password2) < 6:
			args['password_error'] = 'Пароль должен состоять хотя бы из 6 символов'
			return render_to_response('home/change_password.html',args)
		if password1 == password2:
			user.set_password(password1)
			user.save()
			args['success_message'] = 'Ваш пароль успешно изменен'
		else:
			args['password_error'] = 'Пароли не совпадают'
		return render_to_response('home/change_password.html',args)
	else:
		return render_to_response('home/change_password.html',args)


@login_required(login_url=reverse('main:signin'))
def modify_skills(request):
	#init variables
	args = {}
	slogans = Slogan.objects.all()
	args.update(csrf(request))
	owned_skills = request.user.information.skillofuser_set.all().order_by('-experience')
	categories = Category.objects.all().order_by('title')
	all_skills = Skill.objects.all()
	owned_skills_skills = []
	for ownskill in owned_skills:
		owned_skills_skills.append(ownskill.skill)
	args['user'] = request.user
	args['owned_skills_list'] = owned_skills
	args['owned_skills'] = owned_skills_skills
	args['categories'] = categories
	args['all_skills'] = all_skills
	args['slogan'] = slogans[randint(0,slogans.count()-1)]
	
	if request.POST:
		action = request.POST.get('action','')
		if action == 'add':
			experience = request.POST.get('experience','')
			level = request.POST.get('level','')
			skill_id = request.POST.get('skill','')
			new_skill = request.user.information.skillofuser_set.create(experience=experience,skill=Skill.objects.get(pk=skill_id),level= level,user = request.user)
		if action == 'modify':
			experience = request.POST.get('experience','')
			level = request.POST.get('level','')
			skill_id = request.POST.get('skill','')
			skill = get_object_or_404(SkillofUser,pk=skill_id)
			skill.experience = experience
			skill.level = level
			skill.save()

		return redirect(reverse('home:modify_skills'))
	#if user have complated registration 
	if hasattr(request.user, 'information'):
		return render_to_response('home/modify_skills.html',args)
	#if user have not complated registration yet	
	return redirect(reverse('home:create_info'))

@login_required(login_url=reverse('main:signin'))
def delete_skill(request, skill_id):
	#init variables
	args = {}
	user = request.user
	skill = get_object_or_404(SkillofUser,pk=skill_id)
	if skill.user.user == user:
		skill.delete()

	return redirect(reverse('home:modify_skills'))


@login_required(login_url=reverse('main:signin'))
def list_jobs(request, category_id=-1):
	#init variables
	args = {}
	page_ranges = []
	slogans = Slogan.objects.all()
	if hasattr(request.user, 'information'):
		if int(category_id) > 0:
			this_category = get_object_or_404(Category, pk=category_id)
			args['this_category'] = this_category
			jobs = this_category.job_set.all().order_by('-date')
			categories = Category.objects.all().exclude(pk=category_id).order_by('title')
		
		#if category is not choosed
		else:
			jobs = Job.objects.all().order_by('-date')
			categories = Category.objects.all().order_by('title')

		paginator = Paginator(jobs, 10)

		if jobs.count() % 10 == 0:
			page_range = jobs.count()//10;
		else:
			page_range = jobs.count()//10 + 1;

		for i in range(1,page_range+1):
			page_ranges.append(i)
		page = request.GET.get('page')
		try:
			jobs_partial = paginator.page(page)
		except PageNotAnInteger:
			# If page is not an integer, deliver first page.
			jobs_partial = paginator.page(1)
		except EmptyPage:
			# If page is out of range (e.g. 9999), deliver last page of results.
			jobs_partial = paginator.page(paginator.num_pages)

		args['categories'] = categories
		args['page_ranges'] = page_ranges
		args['jobs_partial'] = jobs_partial
		args['slogan'] = slogans[randint(0,slogans.count()-1)]
		args['user'] = request.user
		return render_to_response('home/list_jobs.html',args)
	else:
		return redirect(reverse('home:create_info'))
	# if category is choosed
	


def job_info(request,job_id):
	#init variables
	args = {}
	slogans = Slogan.objects.all()
	
	job = get_object_or_404(Job, pk=job_id)
	args['job'] = job
	args['slogan'] = slogans[randint(0,slogans.count()-1)]
	args['user'] = request.user
	return render_to_response('home/job_info.html',args)
"""

#@login_required(login_url=reverse('main:signin'))
def list_workers(request,category_id = -1):
	#init of variables
	args = {}
	slogans = Slogan.objects.all()
	args.update(csrf(request))
	#if hasattr(request.user, 'information'):

	try:
		int(category_id)
	except Exception, e:
		raise Http404
	if int(category_id) > 0:
		category = get_object_or_404(Category, pk=category_id)
		args['workers'] = Information.objects.filter(category = category).filter(stuff=True)
		categories = Category.objects.all().order_by('id')
		args['this_category'] = category
	else:
		category = get_object_or_404(Category, pk=4)
		args['workers'] = Information.objects.filter(category = category).filter(stuff=True)
		categories = Category.objects.all().order_by('id')
		args['this_category'] = category

	args['categories'] = categories
	args['slogan'] = slogans[0]
	# args['user'] = request.user
	return render_to_response('home/list_workers.html',args)
	#if user hase not registered yet
	#return redirect(reverse('home:create_info'))

def look_profile(request, worker_id):
	#init variables
	args={}
	slogans = Slogan.objects.all()

	
	args['user'] = request.user
	try:
		int(worker_id)
	except Exception, e:
		raise Http404
	
	worker = get_object_or_404(Information, pk=worker_id)
	worker = worker.user
	args['worker'] = worker
	args['slogan'] = slogans[0]
	#owned_skills = worker.information.skillofuser_set.all().order_by('-experience')
	#args['user_skills'] = owned_skills
	return render_to_response('home/look_profile_hire.html',args)

"""
@login_required(login_url=reverse('main:signin'))
def mainpage_hire(request):
	args = {}
	slogans = Slogan.objects.all()
	args.update(csrf(request))
	if request.POST:
		title = request.POST.get('title','')
		description = request.POST.get('description','')
		price = request.POST.get('price','')
		
		category = request.POST.get('category','')
		user = request.user

		category = get_object_or_404(Category, pk=category)
		new_job = Job.objects.create(title = title, description = description, price = price, category = category, user = user)
		new_job.save()
		return redirect(reverse('home:mainpage_hire'))
	else:
		if hasattr(request.user, 'information'):
			args["user"] = request.user
			args['slogan'] = slogans[randint(0,slogans.count()-1)]
			last_registered_workers = Information.objects.all().order_by('-date')[:15]
			args['workers'] = last_registered_workers
			args['categories'] = Category.objects.all()
			return render_to_response('home/mainpage_hire.html',args)
		else:
			return redirect(reverse('home:create_info'))
@login_required(login_url=reverse('main:signin'))
def my_projects(request):
	#init variables
	args = {}
	slogans = Slogan.objects.all()
	args.update(csrf(request))
	user = request.user
	categories = Category.objects.all()
	mine_projects = Job.objects.filter(user=user)
	args['user'] = user
	args['categories'] = categories
	args['my_projects'] = mine_projects
	args['slogan'] = slogans[randint(0,slogans.count()-1)]
	#if user have complated registration
	if hasattr(request.user, 'information'):
		if request.POST:
			title = request.POST.get('title','')
			description = request.POST.get('description','')
			price = request.POST.get('price','')
			period = request.POST.get('period','')
			category = request.POST.get('category','')
			job = get_object_or_404(Job, pk=request.POST.get('job_id',''))
			category = get_object_or_404(Category, pk=category)
			if job.user == request.user:
				#modify a job
				job.title = title
				job.description = description
				job.price = price
				job.period = period
				job.category = category
				job.save()
				args['slogan'] = slogans[randint(0,slogans.count()-1)]
				args['success_message'] = 'Ваш проект успешно отредактирован'
			return render_to_response('home/my_projects.html', args)
		else:
			return render_to_response('home/my_projects.html', args)
			
	#if user have not complated registration
	return redirect(reverse('home:create_info'))

@login_required(login_url=reverse('main:signin'))
def delete_job(request, job_id):
	#init variables
	args = {}
	user = request.user
	job = get_object_or_404(Job, pk=job_id)
	if job.user == user:
		job.delete()

	return redirect(reverse('home:my_projects'))
"""

	


