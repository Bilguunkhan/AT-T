from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserInfo(models.Model):
	user               = models.OneToOneField(User, related_name="info", on_delete=models.CASCADE, null=True)
	location           = models.CharField(max_length=50, blank=True, default='')
	is_teacher         = models.CharField(max_length=50, blank=True, default='')
	interested_subject = models.CharField(max_length=50, blank=True, default='')

class Subject(models.Model):
	tutors      = models.ManyToManyField(User, related_name='tutor_subjects')
	learners    = models.ManyToManyField(User, related_name='learn_subjects')
	name        = models.CharField(max_length=50, blank=True, default='')
	description = models.CharField(max_length=50, blank=True, default='')