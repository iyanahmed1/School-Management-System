from django.urls import path
from StudentPage import views 

app_name='StudentPage'

urlpatterns=[
    path('enrollview/',views.enrollview,name='enrollview'),
    path('studentprofileview/',views.studentprofileview,name='studentprofileview'),
]