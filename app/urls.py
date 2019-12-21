from .pattern import *


urlpatterns = [
	path('getbus/',bus1),
	path('getbus/<int:pk>/',bus2),
	path('getresult/',result1),
	path('getresult/<int:pk>/',result2),
	path('getschool/',school1),
	path('getclass/',class1),
	path('getclass/<int:pk>/',class2),
	path('getschool/<int:pk>/',school2),
	path('getteacher/',teacher1),
	path('getteacher/<int:pk>/',teacher2),
    path('login/',LoginData.as_view(),name='login'),
	path('login_admin/',AdminLogin.as_view()),
	path('school_count/',SchoolCountView.as_view()),
	path('student_count/',StudentCountView.as_view()),
	path('teacher_count/',TeacherCountView.as_view()),
]
