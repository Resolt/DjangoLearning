from django.contrib import admin
from app_one.models import Topic, WebPage, AccessRecord, User

# Register your models here.
admin.site.register(Topic)
admin.site.register(WebPage)
admin.site.register(AccessRecord)
admin.site.register(User)
