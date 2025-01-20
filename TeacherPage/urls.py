from django.urls import path
from . import views

app_name = 'TeacherPage'

urlpatterns = [
    path('login/', views.login_teacher, name='LoginTeacher'),
    path('teacher-dashboard/', views.teacher_dashboard, name='Teacherdashboard'),
    path('manage-attendance/', views.manage_attendance, name='manage_attendance'),
    path('upload-course-material/', views.upload_course_material, name='upload_course_material'),
    path('manage-grades/', views.manage_grades, name='manage_grades'),
    path('submit-feedback/', views.submit_feedback, name='submit_feedback'),
    path('', views.manage_attendance, name='TeacherPage'), 
    path('logout/', views.logout_view, name='Logout'),
]
