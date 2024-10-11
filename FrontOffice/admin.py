from django.contrib import admin

from .models import Inquiry,Appointment,Notification

@admin.register(Inquiry)
class InquiryAdmin(admin.ModelAdmin):
    list_display=['name','email','message','created']

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display=['student','teacher','time','date']

@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display=['recipient','message','createdate']
