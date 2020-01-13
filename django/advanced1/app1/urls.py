from django.contrib import admin
from django.urls import path
from . import views

# TEMPLATE URLS

app_name = 'app1'

urlpatterns = [
	path('admin/', admin.site.urls),
	path('list/', views.SchoolListView.as_view(), name='list'),
	path('list/<int:pk>', views.SchoolDetailView.as_view(), name="detail"),
	path('create/', views.SchoolCreateView.as_view(), name='create'),
	path('update/<int:pk>', views.SchoolUpdateView.as_view(), name='update'),
	path('delete/<int:pk>', views.SchoolDeleteView.as_view(), name='delete'),

	# path('special/', views.special, name="special"),
]
