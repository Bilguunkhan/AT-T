from django.contrib import admin
from .models import UserInfo, Subject, Notification

# Register your models here.
admin.site.register(UserInfo)
admin.site.register(Subject)
admin.site.register(Notification)
