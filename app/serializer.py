from rest_framework import serializers
from .models import User 
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate, login
from django.core import exceptions 
import random

from .models import *
from django.contrib.auth import get_user_model



class UserLogin(serializers.ModelSerializer):
	email=serializers.CharField(max_length=50)
	password=serializers.CharField(max_length=20)
	class Meta:
		model = User
		fields = ('email','password')

	def validate(self,data):
		email=data.get('email')
		password=data.get('password')
		#import pdb ;pdb.set_trace()
		if email and password:
			auth=authenticate(email=email,password=password)
			if auth:
				return auth
			else:
				raise  exceptions.ValidationError('credentials invalid')
		else:
			raise exceptions.ValidationError('fill all the fields')


class TeacherSerailizer(serializers.ModelSerializer):
	class Meta:
		model=Teacher
		fields='__all__'



class SchoolSerailizer(serializers.ModelSerializer):
	class Meta:
		model=School
		fields='__all__'

class ClassSerailizer(serializers.ModelSerializer):
	class Meta:
		model=Class
		fields='__all__'

class BusSerailizer(serializers.ModelSerializer):
	class Meta:
		model=Bus
		fields='__all__'


class ResultSerailizer(serializers.ModelSerializer):
	class Meta:
		model=Result
		fields='__all__'


User = get_user_model()
class  AdminLoginSerializer(serializers.ModelSerializer):
	email=serializers.CharField(max_length=50)
	password=serializers.CharField(max_length=20)
	class Meta:
		model = User
		fields = ('email','password')

	def validate(self,data):
		email=data.get('email')
		password=data.get('password')
		if email and password:
			auth=authenticate(email=email,password=password)
			user = User.objects.get(email = email)
			if auth and user.is_superuser and user.is_staff:
				return auth
			else:
				raise  exceptions.ValidationError('credentials invalid')
		else:
			raise exceptions.ValidationError('fill all the fields')
	

