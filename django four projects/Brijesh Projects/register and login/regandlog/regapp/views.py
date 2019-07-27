from django.shortcuts import render,  HttpResponseRedirect #, redirect,
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import auth
from .models import Profile, Games

def home_view(request):

	return render(request, 'home.html')

def register_view(request):
	
	if request.method=="POST":

		username = request.POST['uname']
		first_name = request.POST['fname']
		last_name = request.POST['lname']
		email = request.POST['email']
		password = request.POST['pwd']
		father_name = request.POST['father_name']
		marks = request.POST['marks']
		

		user,create = User.objects.get_or_create(

			username=username,
			first_name=first_name,
			last_name=last_name,
			email=email,

		)

		
		user.set_password(password)
		user.save()
		pro = Profile(father_name=father_name, marks=marks, user=user)
		pro.save()

		return render(request, 'register.html')
	else:
		return render(request, 'register.html')

def login_view(request):

	if request.method=="POST":

		username = request.POST['uname']
		password = request.POST['pwd']

		try:
			user = auth.authenticate(username=username,password=password)

			if user is not None:
				auth.login(request, user)
				return HttpResponseRedirect('/home/')

			else:
				return render(request, 'login.html', {'msg':'Wrong Username Or Password'})

		except:
			return render(request, 'login.html', {'msg':'Except Block'})

	return render(request, 'login.html', {'msg':'Fresh Page'})	

def logout_view(request):

	auth.logout(request)
	return render(request, 'home.html', {'msg':"LogOut Success"})

def profile_view(request, id=None):

	games = Games.objects.filter(profile=id)

	context = {
		'games':games
	}

	return render(request, 'profile.html', context)

