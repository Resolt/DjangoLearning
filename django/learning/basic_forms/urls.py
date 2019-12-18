from django.conf.urls import url
from django.urls import path
from basic_forms import views

urlpatterns = [
	path('', views.index, name="index"),
	path('formpage', views.form_name, name="form page"),
]
