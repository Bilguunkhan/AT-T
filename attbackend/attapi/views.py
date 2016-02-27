from django.shortcuts import render
from rest_framework import viewsets, generics
from django.contrib.auth.models import User
# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
	queryset = User.objects.all()
	serializer_class = UserSerializer