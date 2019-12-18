from django import forms
from django.core import validators

from app_one.models import User

class Signup(forms.ModelForm):
	first_name = forms.CharField(max_length=100)
	last_name = forms.CharField(max_length=100)
	email = forms.EmailField()
	verify_email = forms.EmailField()  # label="Verify Email"

	class Meta:
		model = User
		fields = ['first_name', 'last_name', 'email']

	def clean(self):
		all_clean_data = super().clean()
		email = all_clean_data['email']
		vemail = all_clean_data['verify_email']

		if email != vemail:
			raise forms.ValidationError("Provided emails do not match")
