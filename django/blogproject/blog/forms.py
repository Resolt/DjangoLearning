from django import forms
from . import models as blog_models


class PostForm(forms.ModelForm):

	class Meta():
		model = blog_models.Post
		fields = ('title', 'text')

		widgets = {
			'title:': forms.TextInput(attrs={'class': 'textinputclass'}),
			'text': forms.Textarea(attrs={'class': 'editable medium-editor-textarea postcontent'})
		}


class CommentForm(forms.ModelForm):

	class Meta():
		model = blog_models.Comment
		fields = ('text',)

		widgets = {
			'text': forms.Textarea(attrs={'class': 'editable medium-editor-textarea'})
		}
