from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
	d = {'insert_me': "I've been inserted from views.py - lel"}
	return render(request, 'app_one/index.html', context=d)
