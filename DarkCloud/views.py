from django.shortcuts import render, reverse
from django.contrib.auth.models import User
from django.contrib.auth import login, logout
from DarkCloud.forms import UserLoginForm
from django.http import HttpResponseRedirect

def index(request):
	return render(request, 'index.html')

def user_login(request):
	if request.method == 'POST':
		form = UserLoginForm(data=request.POST)

		if form.is_valid():
			user = form.get_user()
			login(request, user)
			return HttpResponseRedirect(reverse('index'))
			
	else:
		form = UserLoginForm()
	context = {'form': form}
	return render(request, 'login.html', context)

def user_logout(request):
	logout(request)
	return HttpResponseRedirect(reverse('login'))