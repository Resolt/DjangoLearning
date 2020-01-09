from django.shortcuts import render
from basic_app import forms

from django.http import HttpResponseRedirect, HttpResponse
# from django.core.urlresolvers import reverse
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.backends import ModelBackend

# Create your views here.

def index(request):
	return render(request, 'basic_app/index.html')


@login_required
def user_logout(request):
	logout(request)
	return HttpResponseRedirect(reverse('index'))


def register(request):
	registered = False
	if request.method == "POST":
		user_form = forms.UserForm(data=request.POST)
		profile_form = forms.UserProfileInfoForm(data=request.POST)

		if user_form.is_valid() and profile_form.is_valid():
			user = user_form.save()
			user.set_password(user.password)
			user.save()

			profile = profile_form.save(commit=False)
			profile.user = user

			if 'profile_pic' in request.FILES:
				profile.profile_pic = request.FILES['profile_pic']

			profile.save()

			registered = True

		else:
			print(user_form.errors, profile_form.errors)

	else:
		user_form = forms.UserForm()
		profile_form = forms.UserProfileInfoForm()

	context = {
		'user_form': user_form,
		'profile_form': profile_form,
		'registered': registered
	}

	return render(request, 'basic_app/register.html', context=context)


def user_login(request):

	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')

		user = authenticate(request=request, username=username, password=password)

		if user:
			if user.is_active:
				login(request, user)
				return HttpResponseRedirect(reverse('index'))
			else:
				return HttpResponse("ACCOUNT NOT ACTIVE")
		else:
			print("SOMEONE TRIED TO LOG IN AND FAILED")
			print(username)
			return HttpResponse("INVALID LOGIN DETAILS")
	else:
		return render(request, 'basic_app/login.html')


def special(request):
	return render(request, 'basic_app/special.html')