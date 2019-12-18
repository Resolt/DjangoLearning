from django.conf.urls import url
from django.urls import path
from app_one import views

urlpatterns = [
	path('', views.index, name="index"),
	path('help/', views.help, name="help"),
	path('users/', views.users, name="users"),
	path('signup/', views.signup, name="signup"),
]
