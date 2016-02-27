from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class MyUser(models.Model):
	user               = models.OneToOneField(User)
	location           = models.CharField(max_length=50, blank=True, default='')
	phone_number       = models.CharField(max_length=50, blank=True, default='')
	interested_subject = models.CharField(max_length=50, blank=True, default='')
