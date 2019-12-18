from django.shortcuts import render
from basic_forms import forms
# from django.http import HttpResponse

# Create your views here.
def index(request):
	return render(request, 'basic_forms/index.html')


def form_name(request):

	if request.method == "POST":
		form = forms.FormName(request.POST)
		if form.is_valid():
			print("VALIDATION SUCCESS!")
			print(form.cleaned_data)
	else:
		form = forms.FormName()

	d = {'form':form}
	return render(request, 'basic_forms/forms_page.html', context=d)