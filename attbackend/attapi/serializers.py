from django.contrib.auth.models import User
from rest_framework serializers

class UserSerializer(serializers.ModelSerializer):
	location           = serializers.CharField(source='myuser.location')
	phone_number       = serializers.CharField(source='myuser.phone_number')
	interested_subject = serializers.CharField(source='myuser.interested_subject')
	class Meta:
		model = User
		fields = ('id', 'username', 'email', 'location', 'phone_number', 'interested_subject')