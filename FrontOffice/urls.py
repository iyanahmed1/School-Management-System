from django.urls import path
from FrontOffice import views 

app_name='FrontOffice'

urlpatterns=[
    path('appointmentview/',views.appointmentview,name='appointmentview'),
    path('inquiryview/',views.inquiryview,name='inquiryview'),
    path('registrationview/',views.registrationview,name='registrationview'),
]