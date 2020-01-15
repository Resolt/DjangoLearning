from django import forms
from django.contrib.auth.models import User
from . import models as blog_models


class UserForm(forms.ModelForm):

	password = forms.CharField(widget=forms.PasswordInput())

	class Meta():
		model = User
		fields = ('username', 'password')


class PostForm(forms.ModelForm):

	class Meta():
		model = blog_models.Post
		fields = ('author', 'title', 'text', )

		widgets = {
			'title:': forms.TextInput(attrs={'class': 'textinputclass'}),
			'text': forms.Textarea(attrs={'class': 'editable medium-editor-textarea postcontent'}),
		}


class CommentForm(forms.ModelForm):

	class Meta():
		model = blog_models.Comment
		fields = ('author', 'text')

		widgets = {
			'text': forms.Textarea(attrs={'class': 'editable medium-editor-textarea'}),
		}
