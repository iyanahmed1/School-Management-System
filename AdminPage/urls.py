from django.urls import path
from . import views

app_name = 'AdminPage'

urlpatterns = [
    path('', views.home, name='home'),
    
    path('courses/', views.course_list, name='course_list'),  
    path('courses/create/', views.coursecreate, name='coursecreate'),  
    path('courses/update/', views.courseupdate, name='courseupdate'),
    path('subjects/', views.subjectlist, name='subjectlist'),  
    path('subjects/create/', views.subjectcreate, name='subjectcreate'),
    path('teachers/', views.teacherdetails, name='teacherdetails'), 
    path('students/', views.studentlist, name='studentlist'),
]