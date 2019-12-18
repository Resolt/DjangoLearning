from django.shortcuts import render
from django.http import HttpResponse

from app_one import forms
from app_one.models import Topic, WebPage, AccessRecord, User

# Create your views here.
def index(request):
	webpages_list = AccessRecord.objects.order_by('date')
	d = {
		'insert_me': "I've been inserted from views.py - lel",
		'access_records': webpages_list,
	}
	return render(request, 'app_one/index.html', context=d)


def help(request):
	d = {'help_insert': "HELP PAGE"}
	return render(request, 'app_one/help.html', context=d)


def users(request):
	users_list = User.objects.order_by('last_name')
	d = {'users': users_list}
	return render(request, 'app_one/users.html', context=d)


def signup(request):

	if request.method == "POST":
		form = forms.Signup(request.POST)
		if form.is_valid():
			print("VALIDATION SUCCESS!")
			print(form.cleaned_data)
			form.save(commit=True)
			return index(request)
			# user = form.model
			# user.save()
	else:
		form = forms.Signup()

	d = {'form': form}

	return render(request, 'app_one/signup.html', context=d)
