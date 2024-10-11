from django.contrib import admin
from .models import Attendance,Grade,CourseMaterial,Feedback

@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display=['student_id','subject','attended','date']

@admin.register(Grade)
class GradeAdmin(admin.ModelAdmin):
    list_display=['student_id','subject','grade']

@admin.register(CourseMaterial)
class CourseMaterialAdmin(admin.ModelAdmin):
    list_display=['course','material']

@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display=['user','feedbacktext','date']

