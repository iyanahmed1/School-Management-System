from django import forms
from .models import StudentProfile, Enroll

class StudentProfileForm(forms.ModelForm):
    class Meta:
        model=StudentProfile
        fields=['name','parent_no','email','enrolled_date']

class EnrollForm(forms.ModelForm):
    class Meta:
        model=Enroll
        fields=['name','course','date_enrolled']

        

