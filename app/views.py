from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth.models import User
from .models import *
from .serializer import *
from rest_framework.authtoken.models import Token
from rest_framework import status
from rest_framework import viewsets

from .serializer import AdminLoginSerializer

from .models import School
# Create your views here.


class LoginData(APIView):

	def post(self,request):
		#import pdb;pdb.set_trace()
		serelize=UserLogin(data=request.data)
		#import pdb; pdb.set_trace()
		serelize.is_valid(raise_exception=True)
		objectuser=serelize.validated_data
		#import pdb;pdb.set_trace()
		token, _ = Token.objects.get_or_create(user=objectuser)
		return Response({'token':token.key,'message':'User login successfully'},status=status.HTTP_200_OK,headers={"Access-Control-Allow-Origin":"*"})

class TeacherView(viewsets.ModelViewSet):
	serializer_class=TeacherSerailizer
	queryset=Teacher.objects.all()

class SchoolView(viewsets.ModelViewSet):
	serializer_class=SchoolSerailizer
	queryset=School.objects.all()

class ClassView(viewsets.ModelViewSet):
	serializer_class=ClassSerailizer
	queryset=Class.objects.all()

class BusView(viewsets.ModelViewSet):
	serializer_class=BusSerailizer
	queryset=Bus.objects.all()
class ResultView(viewsets.ModelViewSet):
	serializer_class=ResultSerailizer
	queryset=Result.objects.all()


class AdminLogin(APIView):

	def post(self,request):
		serializer = AdminLoginSerializer
		serializer=AdminLoginSerializer(data=request.data)
		serializer.is_valid(raise_exception=True)
		objectuser=serializer.validated_data
		
		token, _ = Token.objects.get_or_create(user=objectuser)
		return Response({'token':token.key,'message':'User login successfully'},status=status.HTTP_200_OK,headers={"Access-Control-Allow-Origin":"*"})

class SchoolCountView(APIView):
	def get(self,request):
		count = School.objects.all().count()
		return Response({"count":count})

class TeacherCountView(APIView):
	def get(self,request):
		count = Teacher.objects.all().count()
		return Response({"count":count})

class StudentCountView(APIView):
	def get(self,request):
		count = Student.objects.all().count()
		return Response({"count":count})




