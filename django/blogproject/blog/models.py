from django.db import models
from django.utils import timezone
from django.urls import reverse

# Create your models here.

class Post(models.Model):
	author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
	title = models.CharField(max_length=256)
	text = models.CharField(max_length=4096)
	create_date = models.DateTimeField(default=timezone.now)
	pub_date = models.DateTimeField(blank=True, null=True)

	def publish(self):
		self.pub_date = timezone.now()
		self.save()

	def approve_comments(self):
		return self.comments.filter(appr_comment=True)

	def get_absolute_url(self):
		return reverse('post_detail', kwargs={'pk':self.pk})

	def __str__(self):
		return self.title


class Comment(models.Model):
	post = models.ForeignKey('blog.Post', related_name='comments', on_delete=models.CASCADE)
	# author = models.ForeignKey('blog.Post', on_delete=models.CASCADE)
	text = models.CharField(max_length=1024)
	create_date = models.DateTimeField(default=timezone.now)
	appr_comment = models.BooleanField(default=False)

	def approve(self):
		self.appr_comment = True
		self.save()

	def get_absolute_url(self):
		return reverse('post_list')

	def __str__(self):
		return self.text