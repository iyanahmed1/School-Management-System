from django.contrib import admin
from .models import Student,Teacher,Subject,Course,Feedback

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display=['name','enrolled_date'] 

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display=['first_name','last_name','hiredate']

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display=['name','slug']
    prepopulated_fields={'slug':('name',)}

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display=['name','subject','created']
    list_filter=['subject','created']
    search_fields=['name']
    prepopulated_fields={'slug':('name',)}
    
#@admin.register(Attendance)
#class AttendanceAdmin(admin.ModelAdmin):
#    list_display=['student','subject','date','attended']

@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display=['sender','receiver','message','date']