from django.contrib import admin
from .models import StudentProfile,StudentGrade,Attend,StudentFeedback,Enrollment

@admin.register(StudentProfile)
class StudentProfileAdmin(admin.ModelAdmin):
    list_display=['student','course','email','date_of_birth']

@admin.register(StudentGrade)
class StudentGradeAdmin(admin.ModelAdmin):
    list_display=['student','course','grade','date']

@admin.register(Attend)
class AttendAdmin(admin.ModelAdmin):
    list_display=['student','course','date','attended']

@admin.register(StudentFeedback)
class StudentFeedbackAdmin(admin.ModelAdmin):
    list_display=['student','message','teacher','adminresponse','submitdate']

@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display=['student','course','enrollment_date']
