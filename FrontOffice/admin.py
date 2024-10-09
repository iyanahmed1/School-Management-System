from django.contrib import admin
from .models import  Registration,Appointment,Notification,inquiry

@admin.register(Registration)
class RegistrationAdmin(admin.ModelAdmin):
    list_display=['student_name','course']

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display=['teacher','student','reason','date']

@admin.register(Notification)
class NotifactionAdmin(admin.ModelAdmin):
    list_display=['student','parent','message']

@admin.register(inquiry)
class inquiryAdmin(admin.ModelAdmin):
    list_display=['people','date','note']