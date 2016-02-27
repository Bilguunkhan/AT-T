from django.contrib.auth.models import User
from rest_framework import serializers
from .models import MyUser

class UserSerializer(serializers.ModelSerializer):
	#username           = serializers.CharField(source='user.username')
	#email              = serializers.CharField(source='user.email')
	#password           = serializers.CharField(source='user.password')
	location           = serializers.CharField(source='myuser.location')
	phone_number       = serializers.CharField(source='myuser.phone_number')
	interested_subject = serializers.CharField(source='myuser.interested_subject')
	class Meta:
		model = User
		fields = ('id', 'username', 'email', 'password', 'location', 'phone_number', 'interested_subject')

	def restore_object(self, attrs, instance=None):
		if instance is not None:
			instance.user.email    = attrs.get('user.email', instance.user.email)
			instance.user.password = attrs.get('user.password', instance.user.password)
			instance.location      = attrs.get('location', instance.location)
			instance.phone_number  = attrs.get('phone_number', instance.phone_number)
			instance.interested_subject = attrs.get('interested_subject', instance.interested_subject)
			return instance
		user = User.objects.create_user(
			username=attrs.get('user.username'), 
			email=attrs.get('user.email'), 
			password=attrs.get('user.password') 
			)
		return MyUser(user=user)