from django.shortcuts import (
	render,
	get_object_or_404,
	redirect,
)
from django.views.generic import (
	TemplateView,
	ListView,
	DetailView,
	CreateView,
	UpdateView,
	DeleteView,
)
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from . import models as blog_models
from . import forms as blog_forms

# Create your views here.

class AboutView(TemplateView):
	template = 'blog/about.html'


class PostListVew(ListView):
	model = blog_models.Post

	def get_queryset(self):
		return blog_models.Post.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')


class PostDetailView(DetailView):
	model = blog_models.Post


class PostCreateView(LoginRequiredMixin, CreateView):
	login_url = '/login/'
	model = blog_models.Post
	redirect_field_name = 'blog/post_detail.html'
	form_class = blog_forms.PostForm


class PostUpdateView(LoginRequiredMixin, UpdateView):
	login_url = '/login/'
	model = blog_models.Post
	redirect_field_name = 'blog/post_detail.html'
	form_class = blog_forms.PostForm


class PostDeleteView(LoginRequiredMixin, DeleteView):
	model = blog_models.Post
	success_url = reverse_lazy('post_list')


class DraftListView(LoginRequiredMixin, ListView):
	login_url = '/login/'
	redirect_field_name = 'blog/post_list.html'
	model = blog_models.Post

	def get_queryset(self):
		return blog_models.Post.objects.filter(pub_date__isnull=True).order_by('create_date')


@login_required
def post_publish(request, pk):
	post = get_object_or_404(blog_models.Post, pk=pk)
	post.publish()
	return redirect('post_detail', pk=pk)


@login_required
def add_comment_to_post(request, pk):
	post = get_object_or_404(blog_models.Post, pk=pk)
	if request.method == 'POST':
		form = blog_forms.CommentForm(request.POST)
		if form.is_valid():
			comment = form.save(commit=False)
			comment.post = post
			return redirect('post_detail', pk=post.pk)
	else:
		form = blog_forms.CommentForm()
	context = {'form': form}
	return render(request, 'blog/comment_form.html', context=context)


@login_required
def comment_approve(request, pk):
	comment = get_object_or_404(blog_models.Comment, pk=pk)
	comment.approve()
	return redirect('post_detail', pk=comment.post.pk)


@login_required
def comment_remove(request, pk):
	comment = get_object_or_404(blog_models.Comment, pk=pk)
	post_pk = comment.post.pk
	comment.delete()
	return redirect('post_detail', pk=post_pk)
