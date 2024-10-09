from django import forms
from .models import Grade,Attendance

class GradeForm(forms.ModelForm):
    class Meta:
        model=Grade
        fields=['student','subject','grade']

class AttendanceForm(forms.ModelForm):
    class Meta:
        model=Attendance
        fields=['student','subject','date','attended']