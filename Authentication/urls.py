from django.urls import path
from . import views

app_name = "Authentication"

urlpatterns = [
    path("login/", views.login_user, name="login"),
    path("logout/", views.logout_user, name="logout"),
    path("teacher-dashboard/", views.teacher_dashboard, name="Teacherdashboard"),
    path("student-dashboard/", views.student_dashboard, name="StudentDashboard"),
]
