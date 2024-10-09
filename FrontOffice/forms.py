from django import forms
from .models import Registration, inquiry,Appointment

class RegistrationForm(forms.ModelForm):
    class Meta:
        model=Registration
        fields=['student_name','location','email','parent_no','course']

class inquiryForm(forms.ModelForm):
    class Meta:
        model=inquiry
        fields=['people','note','date']

class AppointmentForm(forms.ModelForm):
    class Meta:
        model=Appointment
        fields=['teacher','student','reason']