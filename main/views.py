from django.shortcuts import render_to_response, redirect
from django.contrib.auth.models import User
from django.core.context_processors import csrf
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login, logout
from django.template import RequestContext
from home.models import Mail

def mainpage(request):
	#init variables
	args={}
	args.update(csrf(request))

	if request.user.is_authenticated():
		return redirect(reverse("home:mainpage"))
	else:
		if request.POST:
			name = request.POST['name']
			email = request.POST['email']
			subject = request.POST['subject']
			message = request.POST['message']

			mail = Mail.objects.create(name=name, email=email, title=subject, body=message)
			mail.save()
			args['success_message'] = "Ваше сообщение успешно отправлено."
			return render_to_response('main/mainpage.html',args)
		else:
			return render_to_response('main/mainpage.html',args)
"""
def signin(request):
	if request.user.is_authenticated():
		return redirect(reverse("home:mainpage"))
	#initialize variables
	args={}
	args.update(csrf(request))

	if request.POST:
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		if user is not None:
			if user.is_active:
				login(request, user)
				return redirect(reverse("home:mainpage"))
			else:
				args['signin_error'] = "ваш аккаунт временно заблокирован"
				args['username'] = username
				args['password'] = password
				return render_to_response('main/signin.html',args)
		else:
			args['signin_error'] = "Имя пользователя и пароль не совпадают"
			args['username'] = username
			args['password'] = password
			return render_to_response('main/signin.html',args)
	else:
		return render_to_response('main/signin.html',args)

def signout(request):
    logout(request)
    return redirect(reverse('main:mainpage'))

def signup(request):
	if request.user.is_authenticated():
		return redirect(reverse("home:mainpage"))
	#initialize variables
	args={}
	args.update(csrf(request))
	validation = True
	all_users = User.objects.all()

	if request.POST:
		first_name = request.POST.get('firstname','')
		last_name = request.POST.get('lastname','')
		username = request.POST.get('username','')
		password1 = request.POST.get('password','')
		password2 = request.POST.get('password1','')
		email = request.POST.get('email','')
		#posted data validation
		#first_name validation
		if len(first_name) < 2 :
			args['first_name_error'] = 'Слишком короткое имя'
			validation = False
			args['first_name'] = first_name
		else:
			args['first_name'] = first_name
		if len(last_name) < 2 :
		#last_name validation
			args['last_name_error'] = 'Слишком короткая фамилия '
			validation = False
			args['last_name'] = last_name
		else:
			args['last_name'] = last_name
		#username validation
		if len(username) > 2:
			username_in_use = all_users.filter(username__iexact=username)
			if username_in_use.count() > 0:
				validation = False
				args['username_error'] = 'Этот логин уже занят,выберите другой'
				args['username'] = username
			else:
				args['username'] = username
		else:
			args['username_error'] = 'Слишком короткий логин'
		#password validation
		if len(password1) < 6 or len(password2) < 6:
			validation = False
			args['password_error'] = 'Пароль должен состоять хотя бы из 6 символов'
		#email validation
		email_in_use = all_users.filter(email=email)
		if email_in_use.count() > 0:
			validation = False
			args['email_error'] = 'Этот email уже используется, используйте другой'
			args['email'] = email 
		else:
			args['email'] = email

		if validation == False:
			return render_to_response('main/signup.html', args)

		if password1 == password2:
			user = User.objects.create_user(username, email, password1)
			user.first_name = first_name
			user.last_name = last_name
			user.save()
			args['success_message'] = 'Вы успешно зарегистрированы и можете уже авторизоваться'
			return render_to_response('main/signin.html',args)
		else:
			args['password_error'] = 'Пароли не совпадают'
			return render_to_response('main/signup.html',args)

	else:
		return render_to_response('main/signup.html',args)
"""