from django.shortcuts import render, redirect


# Create your views here.

from django.contrib.auth import (
	authenticate,
	get_user_model,
	login as login_auth,
	logout as logout_auth,

	)

from django.contrib import auth
from .forms import LoginForm, RegisterForm

from django.contrib import messages

User = get_user_model()

import hashlib

def register(request, *args, **kwargs):
	form = RegisterForm(request.POST)
	if request.method == 'POST' and form.is_valid():
		user = form.save(commit=False)
		
		username = form.cleaned_data.get("username")
		email = form.cleaned_data.get("email")
		password = form.cleaned_data.get("password")

		username_qs = User.objects.filter(username=username)
		if username_qs.exists():
			print('user existe')
			
			messages.error(request, "Error")

			return redirect("/registro")

		else:
			
			user = User.objects.create(username=username, email=email, password=password)
			user.set_password(password)
			user.save()
			user_auth = authenticate(username=username, password=password)
			login_auth(request, user_auth)
			return redirect("/")	

	else: 
		print(form)

	context = {

		"form": form,

	}

	return render(request, "register.html", context)




from django.contrib.auth.decorators import login_required


def login(request):
	form = LoginForm(request.POST or None)    

	if request.method == 'POST' and form.is_valid():
		print(form.cleaned_data)

		user = form.authenticate_user()
		login_auth(request, user)
		return redirect('/')

	return render(request, 'login.html',{'form': form})



@login_required
def logout(request):
	logout_auth(request)
	return  redirect('/')


def index(request):
	return render(request, 'index.html')


