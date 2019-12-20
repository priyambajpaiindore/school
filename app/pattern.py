from django.contrib import admin
from django.urls import path,include
from .views import *
teacher1=TeacherView.as_view({
	'get':'list',
	'post':'create',
	})
teacher2=TeacherView.as_view({
	'put':'update',
	'patch':'partial_update',
	'get':'retrieve',
	'delete':'destroy'
	})

school1=SchoolView.as_view({
	'get':'list',
	'post':'create',
	})
school2=SchoolView.as_view({
	'put':'update',
	'patch':'partial_update',
	'get':'retrieve',
	'delete':'destroy'
	})

class1=ClassView.as_view({
	'get':'list',
	'post':'create',
	})
class2=ClassView.as_view({
	'put':'update',
	'patch':'partial_update',
	'get':'retrieve',
	'delete':'destroy'
	})

bus1=BusView.as_view({
	'get':'list',
	'post':'create',
	})
bus2=BusView.as_view({
	'put':'update',
	'patch':'partial_update',
	'get':'retrieve',
	'delete':'destroy'
	})
result1=ResultView.as_view({
	'get':'list',
	'post':'create',
	})
result2=ResultView.as_view({
	'put':'update',
	'patch':'partial_update',
	'get':'retrieve',
	'delete':'destroy'
	})