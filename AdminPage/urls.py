from django.urls import path
from AdminPage import views 

app_name='AdminPage'

urlpatterns=[
    path('courseview/',views.courseview,name='courseview'),
    path('studenview/',views.studentview,name='studentview'),
    path('subjectview/',views.subjectview,name='subjectview'),
    path('teacherview/',views.teacherview,name='teacherview')
]