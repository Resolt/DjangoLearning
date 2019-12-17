import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'learning.settings')

import django
django.setup()

import random
from app_one.models import Topic, WebPage, AccessRecord

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


if __name__ == '__main__':
	print("populating..")
	populate(20)
	print('done!')

