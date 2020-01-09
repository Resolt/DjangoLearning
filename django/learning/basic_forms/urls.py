from django.conf.urls import url
from django.urls import path
from basic_forms import views

app_name = "basic_forms"

urlpatterns = [
	path('', views.index, name="index"),
	path('formpage', views.form_name, name="form page"),
]
