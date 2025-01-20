from django.urls import path
from . import views

app_name = 'FrontOffice'

urlpatterns = [
    path('login/', views.login_staff, name='LoginStaff'),
    path('staff-dashboard/', views.staff_dashboard, name='StaffDashboard'),
    path('register/', views.register_student, name='register_student'), 
    path('inquiry/', views.submit_inquiry, name='submit_inquiry'),  
    path('inquiry/success/', views.inquiry_success, name='inquiry_success'),
    path('appointment/', views.schedule_appointment, name='schedule_appointment'), 
    path('register/success/', views.register_success, name='register_success'), 
    path('appointment-success/', views.appointment_success, name='appointment_success'),
    path('notification/', views.send_notification, name='send_notification'), 
    path('notification/success/', views.notification_success, name='notification_success'),  
]
