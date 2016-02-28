from django.contrib.auth.models import User
from rest_framework import serializers
from .models import UserInfo, Subject, Notification

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model  = User
		fields = ('id', 'username', 'email', 'password')
	def create(self, validated_data):
		user = super(UserSerializer, self).create(validated_data)
		if 'password' in validated_data:
			user.set_password(validated_data['password'])
			user.save()
		return user

class UserInfoSerializer(serializers.ModelSerializer):
	class Meta:
		model  = UserInfo
		fields = ('id', 'user', 'location', 'is_teacher', 'interested_subject')

class SubjectSerializer(serializers.ModelSerializer):
	class Meta:
		model  = Subject
		fields = ('id', 'name', 'description', 'tutors', 'learners')

class NotificationSerializer(serializers.ModelSerializer):
	class Meta:
		model  = Notification
		fields = ('id', 'tutor_user', 'learner_user', 'subject')  