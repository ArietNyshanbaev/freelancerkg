#importings
from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.core.context_processors import csrf
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login, logout
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Information , SkillofUser , Skill , Category , Job

# Views
@login_required(login_url=reverse('main:signin'))
def mainpage(request):
	#initialize variables
	args={}
	#if user have complated registration
	if hasattr(request.user, 'information'):
		args["user"] = request.user
		last_jobs = Job.objects.all().order_by('-date')[:15]
		args['last_jobs'] = last_jobs
		return render_to_response('home/mainpage.html',args)
	#if user have not complated registration return him to complate registration page
	return redirect(reverse('home:create_info'))

@login_required(login_url=reverse('main:signin'))
def profile(request):
	#init variables
	args={}
	#if user have complated registration
	if hasattr(request.user, 'information'):
		args['user'] = request.user
		return render_to_response('home/profile.html',args)
	else:
		return redirect(reverse('home:create_info'))

@login_required(login_url=reverse('main:signin'))
def create_info(request):
	#initialize variables
	args={}
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
		address = request.POST.get('address','')
		category_id = request.POST.get('category','')
		category = Category.objects.get(pk=category_id)
		information = Information.objects.create(user = user,image = image, gender = gender, category = category, born_date = born_date, phone_number = phone_number, address = address)
		information.save()
		return redirect(reverse('home:mainpage'))
	else:
		categories = Category.objects.all()
		args['categories'] = categories
		args['user'] = request.user

		return render_to_response('home/create_info.html',args)

@login_required(login_url=reverse('main:signin'))
def modify_info(request):
	#initialize variables
	args={}
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
		user.information.save()
		user.save()
		args['user'] = request.user
		args['success_message'] = 'Профиль успешно отредактирован'
		return render_to_response('home/profile.html',args)
	else:
		#if user have complated registration
		if hasattr(request.user, 'information'):
			args["user"] = request.user
			return render_to_response('home/modify_info.html',args)
		else:
			return redirect(reverse('home:create_info'))

@login_required(login_url=reverse('main:signin'))
def modify_skills(request):
	#init variables
	args = {}
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
	if hasattr(request.user, 'information'):
		if int(category_id) > 0:
			this_category = get_object_or_404(Category, pk=category_id)
			args['this_category'] = this_category
			args['jobs'] = this_category.job_set.all().order_by('-date')
			categories = Category.objects.all().exclude(pk=category_id).order_by('title')
		
		#if category is not choosed
		else:
			args['jobs'] = Job.objects.all().order_by('-date')
			categories = Category.objects.all().order_by('title')

		args['categories'] = categories
		args['user'] = request.user
		return render_to_response('home/list_jobs.html',args)
	else:
		return redirect(reverse('home:create_info'))
	# if category is choosed
	

@login_required(login_url=reverse('main:signin'))
def job_info(request,job_id):
	#init variables
	args = {}
	if hasattr(request.user, 'information'):
		job = get_object_or_404(Job, pk=job_id)
		args['job'] = job
		args['user'] = request.user
		return render_to_response('home/job_info.html',args)
	#if user hase not registered yet
	return redirect(reverse('home:create_info'))

@login_required(login_url=reverse('main:signin'))
def list_workers(request,category_id = -1):
	#init of variables
	args = {}
	if hasattr(request.user, 'information'):
		if int(category_id) > 0:
			category = get_object_or_404(Category, pk=category_id)
			args['workers'] = Information.objects.filter(category = category)
			categories = Category.objects.all().exclude(pk = category_id).order_by('title')
			args['this_category'] = category
		else:
			args['workers'] = Information.objects.all()
			categories = Category.objects.all().order_by('title')
		args['categories'] = categories
		args['user'] = request.user
		return render_to_response('home/list_workers.html',args)
	#if user hase not registered yet
	return redirect(reverse('home:create_info'))

@login_required(login_url=reverse('main:signin'))
def look_profile(request, key, worker_id):
	#init variables
	args={}
	#if user have complated registration
	if hasattr(request.user, 'information'):
		args['user'] = request.user
		worker = get_object_or_404(Information, pk=worker_id)
		worker = worker.user
		args['worker'] = worker
		if int(key) == 1:
			return render_to_response('home/look_profile_work.html',args)
		owned_skills = request.user.information.skillofuser_set.all().order_by('-experience')
		args['user_skills'] = owned_skills
		return render_to_response('home/look_profile_hire.html',args)
	#if user have not complated registration
	return redirect(reverse('home:create_info'))

@login_required(login_url=reverse('main:signin'))
def mainpage_hire(request):
	args = {}
	args.update(csrf(request))
	if request.POST:
		title = request.POST.get('title','')
		description = request.POST.get('description','')
		price = request.POST.get('price','')
		period = request.POST.get('period','')
		category = request.POST.get('category','')
		user = request.user

		category = get_object_or_404(Category, pk=category)
		new_job = Job.objects.create(title = title, description = description, price = price, period = period, category = category, user = user)
		new_job.save()
		return redirect(reverse('home:mainpage_hire'))
	else:
		if hasattr(request.user, 'information'):
			args["user"] = request.user
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
	args.update(csrf(request))
	user = request.user
	categories = Category.objects.all()
	mine_projects = Job.objects.filter(user=user)
	args['user'] = user
	args['categories'] = categories
	args['my_projects'] = mine_projects
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
	


