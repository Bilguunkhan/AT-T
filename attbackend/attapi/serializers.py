from django.contrib.auth.models import User
from rest_framework import serializers
from .models import UserInfo

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model  = User
		fields = ('id', 'username', 'email', 'password', 'info')
	def create(self, validated_data):
		user = super(UserSerializer, self).create(validated_data)
		if 'password' in validated_data:
			user.set_password(validated_data['password'])
			user.save()
		return user

class UserInfoSerializer(serializers.ModelSerializer):
	class Meta:
		model  = UserInfo
		fields = ('id', 'user', 'location', 'phone_number', 'interested_subject')