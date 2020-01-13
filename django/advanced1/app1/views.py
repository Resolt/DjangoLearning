from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import View, TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.http import HttpResponse

from . import models

# Create your views here.


# def index(request):
# 	return render(request, 'index.html')


# class CBView(View):
# 	def get(self, request):
# 		return HttpResponse('CBV BITHC')


class IndexView(TemplateView):
	template_name = "index.html"

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context.update({'injectme': 'THIS IS INJECTED FROM CONTEXT - TEST'})
		return context


class SchoolListView(ListView):
	context_object_name = 'schools'
	model = models.School
	template_name = "app1/school_list.html"


class SchoolDetailView(DetailView):
	context_object_name = 'school_detail'
	model = models.School
	template_name = "app1/school_detail.html"


class SchoolCreateView(CreateView):
	# context_object_name = 'school_create'
	model = models.School
	template_name = "app1/school_form.html"
	fields = ('name', 'principal', 'location')


class SchoolUpdateView(UpdateView):
	# context_object_name = 'school_update'
	model = models.School
	# template_name = "app1/school_update.html"
	fields = ('name', 'principal')


class SchoolDeleteView(DeleteView):
	# context_object_name = 'school_delete'
	model = models.School
	template_name = "app1/school_confirm_delete.html"
	success_url = reverse_lazy('app1:list')
