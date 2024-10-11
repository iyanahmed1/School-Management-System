from django.contrib import admin
from .models import Teacher,Student,Subject,Course

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display=['first_name','last_name','subject']

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display=['student_id','first_name','last_name','course']

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display=['subjectname']

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display=['course_id','coursename']

