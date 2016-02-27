from django.shortcuts import render
from rest_framework import viewsets, generics
from django.contrib.auth.models import User
from .serializers import UserSerializer, UserInfoSerializer, SubjectSerializer
from .models import UserInfo, Subject
# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
	queryset = User.objects.all()
	serializer_class = UserSerializer

class UserInfoViewSet(viewsets.ModelViewSet):
	queryset = UserInfo.objects.all()
	serializer_class = UserInfoSerializer

class SubjectViewSet(viewsets.ModelViewSet):
	queryset = Subject.objects.all()
	serializer_class = SubjectSerializer