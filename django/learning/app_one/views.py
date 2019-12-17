from django.shortcuts import render
from django.http import HttpResponse
from app_one.models import Topic, WebPage, AccessRecord

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

