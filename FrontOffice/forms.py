from django import forms
from .models import Inquiry,Appointment,Notification

class InquiryForm(forms.ModelForm):
    class Meta:
        model=Inquiry
        fields=['name','email','message','created']

class AppointmentForm(forms.ModelForm):
    class Meta:
        model=Appointment
        fields=['student','teacher','time','date']

class NotificationForm(forms.ModelForm):
    class Meta:
        model=Notification
        fields=['recipient','message','createdate']

