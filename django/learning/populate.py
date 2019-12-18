import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'learning.settings')

import django
django.setup()

import random
from app_one.models import Topic, WebPage, AccessRecord, User

from faker import Faker

fakegen = Faker()

topics = ['Search', 'Social', 'Marketplace', 'News', 'Games']

def add_topic():
	t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
	t.save()
	return t

def populate(N=5):

	for entry in range(N):
		topic = add_topic()

		fake_url = fakegen.url()
		fake_date = fakegen.date()
		fake_name = fakegen.company()

		webpg = WebPage.objects.get_or_create(topic=topic, url=fake_url, name=fake_name)[0]
		accrc = AccessRecord.objects.get_or_create(name=webpg, date=fake_date)[0]


def add_user():
	first_name = fakegen.first_name()
	last_name = fakegen.last_name()
	email = fakegen.email()

	user = User.objects.get_or_create(first_name=first_name, last_name=last_name, email=email)[0]
	# user.save()


def populate_users(N=5):
	for _ in range(N):
		add_user()


if __name__ == '__main__':
	print("populating..")
	# populate(20)
	populate_users(20)
	print('done!')

