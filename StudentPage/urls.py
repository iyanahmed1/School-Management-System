from django.urls import path
from . import views

app_name = 'StudentPage'  

urlpatterns = [
   path('login/',views.login_student, name='LoginStudent'),
    path('dashboard/', views.student_dashboard, name='StudentDashboard'),
    path('student_profile/<int:id>/', views.student_profile, name='student_profile'),
    path('student_enrollment/', views.student_enrollment, name='student_enrollment'),
    path('student_grade/', views.student_grade, name='student_grade'),
    path('student_attendance/', views.student_attendance, name='student_attendance'),
    path('student_feedback/', views.student_feedback, name='student_feedback'),
    path('profile_success/', views.profile_success, name='profile_success'),
    path('enrollment_success/', views.enrollment_success, name='enrollment_success'),
    path('grade_success/', views.grade_success, name='grade_success'),
    path('attendance_success/', views.attendance_success, name='attendance_success'),
    path('feedback_success/', views.feedback_success, name='feedback_success'),
    path("logout/", views.logout_view, name="logout"),
]
