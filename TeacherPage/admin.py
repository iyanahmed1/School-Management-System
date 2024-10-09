from django.contrib import admin
from .models import Grade,CourseMaterial,Attendance

@admin.register(Grade)
class GradeAdmin(admin.ModelAdmin):
    list_display=['student','subject','grade']
    search_fields=['student','subject']


@admin.register(CourseMaterial)
class CourseMaterialAdmin(admin.ModelAdmin):
    list_display=['course','material']

@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display=['student','subject','date','attended']
