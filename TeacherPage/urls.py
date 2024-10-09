from django.urls import path
from TeacherPage import views 

app_name='TeacherPage'

urlpatterns=[
    path('attendanceview/',views.attendanceview,name='attendanceview'),
    path('gradeview/',views.gradeview,name='gradeview'),
]