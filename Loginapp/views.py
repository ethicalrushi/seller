from django.shortcuts import render
from django.contrib.auth.models import User
from .forms import UserForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,logout,authenticate
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse



# Create your views here.

def register(request):

	registered = False

	if request.method == "POST":
		user_form = UserForm(data=request.POST)
		
		if user_form.is_valid():

			user = user_form.save()
			user.set_password(user.password)
			user.save()

			

			registered = True

		else:
			print(user_form.errors)

	else:
		user_form = UserForm()

	return render(request,'Loginapp/registeration.html',
		                   {'user_form':user_form,
		                    
		                    'registered':registered,
							})

def user_login(request):

	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')

		user = authenticate(username=username, password=password)

		if user:
			if user.is_active:
				login(request,user)
				return HttpResponseRedirect('/product/')

			else:
				return HttpResponse("Account Not Active")

		else:
			print("Someone tried to login and failed!")
			return HttpResponse("Invalid login details")

	else:
		return render(request,'Loginapp/login.html')

@login_required
def user_logout(request):
	logout(request)
	return render(request,'basic_app/index.html')
