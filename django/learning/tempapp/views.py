from django.shortcuts import render

# Create your views here.
def index(request):
	context = {'text':'hello world','number':42}
	return render(request, 'tempapp/index.html', context=context)

def other(request):
	return render(request, 'tempapp/other.html')

def relative(request):
	return render(request, 'tempapp/relative.html')