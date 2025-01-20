from django.urls import path
from . import views

app_name = 'AdminPage'

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_admin, name='LoginAdmin'),
    path('admin-dashboard/', views.admin_dashboard, name='AdminDashboard'),
    path('register-student/', views.register_student, name='register_student'),
    path('courses/', views.course_list, name='course_list'),  
    path('courses/create/', views.coursecreate, name='coursecreate'),  
    path('courses/update/', views.courseupdate, name='courseupdate'),
    path('subjects/', views.subjectlist, name='subjectlist'),  
    path('subjects/create/', views.subjectcreate, name='subjectcreate'),
    path('teachers/', views.teacherdetails, name='teacherdetails'), 
    path('students/', views.studentlist, name='studentlist'),
    path('logout/', views.logout_view, name='Logout'),
]
