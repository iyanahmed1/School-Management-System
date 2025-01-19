from django import forms
from .models import Inquiry,Appointment,Notification,StudentRegistration

class StudentRegistrarionForm(forms.ModelForm):
    class Meta:
        model=StudentRegistration
        fields=['first_name','last_name','location','email']
        exclude = ['date']
class InquiryForm(forms.ModelForm):
    class Meta:
        model=Inquiry
        fields=['name','email','message']

class AppointmentForm(forms.ModelForm):
    class Meta:
        model=Appointment
        fields=['student','teacher','time','date']

class NotificationForm(forms.ModelForm):
    class Meta:
        model=Notification
        fields=['recipient','message']


form = StudentRegistrarionForm()
print(form.fields)