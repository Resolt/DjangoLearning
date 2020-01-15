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
	DeleteView
)

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from django.http import HttpResponseRedirect, HttpResponse

from django.urls import reverse_lazy, reverse
from django.utils import timezone

from . import models as blog_models
from . import forms as blog_forms

# Create your views here.


class AboutView(TemplateView):
	template_name = 'blog/about.html'


class PostListView(ListView):
	model = blog_models.Post

	def get_queryset(self):
		return blog_models.Post.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')


class PostDetailView(DetailView):
	model = blog_models.Post


class PostCreateView(LoginRequiredMixin, CreateView):
	login_url = 'blog:login'
	model = blog_models.Post
	redirect_field_name = 'blog/post_detail.html'
	# redirect_field_name = 'blog:post_detail'
	form_class = blog_forms.PostForm


class PostUpdateView(LoginRequiredMixin, UpdateView):
	login_url = 'blog:login'
	model = blog_models.Post
	redirect_field_name = 'blog/post_detail.html'
	form_class = blog_forms.PostForm


class PostDeleteView(LoginRequiredMixin, DeleteView):
	model = blog_models.Post
	success_url = reverse_lazy('blog:post_list')


class DraftListView(LoginRequiredMixin, ListView):
	login_url = 'blog:login'
	redirect_field_name = 'blog/post_draft_list.html'
	model = blog_models.Post

	def get_queryset(self):
		return blog_models.Post.objects.filter(pub_date__isnull=True).order_by('create_date')


def user_login(request):

	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')

		user = authenticate(request=request, username=username, password=password)

		if user:
			if user.is_active:
				login(request, user)
				return HttpResponseRedirect(reverse('blog:post_list'))
			else:
				return HttpResponse("ACCOUNT NOT ACTIVE")
		else:
			print("SOMEONE TRIED TO LOG IN AND FAILED")
			print(username)
			return HttpResponse("INVALID LOGIN DETAILS")
	else:
		return render(request, 'blog/login.html')


@login_required
def user_logout(request):
	logout(request)
	return HttpResponseRedirect(reverse('blog:post_list'))


@login_required
def post_publish(request, pk):
	post = get_object_or_404(blog_models.Post, pk=pk)
	post.publish()
	return redirect('blog:post_detail', pk=pk)


@login_required
def add_comment_to_post(request, pk):
	post = get_object_or_404(blog_models.Post, pk=pk)
	if request.method == 'POST':
		form = blog_forms.CommentForm(request.POST)
		if form.is_valid():
			comment = form.save(commit=False)
			comment.post = post
			comment.save()
			return redirect('blog:post_detail', pk=post.pk)
	else:
		form = blog_forms.CommentForm()
	context = {'form': form}
	return render(request, 'blog/comment_form.html', context=context)


@login_required
def comment_approve(request, pk):
	comment = get_object_or_404(blog_models.Comment, pk=pk)
	comment.approve()
	return redirect('blog:post_detail', pk=comment.post.pk)


@login_required
def comment_remove(request, pk):
	comment = get_object_or_404(blog_models.Comment, pk=pk)
	post_pk = comment.post.pk
	comment.delete()
	return redirect('blog:post_detail', pk=post_pk)
