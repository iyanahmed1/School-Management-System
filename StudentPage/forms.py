from django import forms
from .models import StudentProfile, Enrollment, StudentGrade, Attend,StudentFeedback

class StudentProfileForm(forms.ModelForm):
    class Meta:
        model=StudentProfile
        fields=['student','course','email','date_of_birth']

class EnrollmentForm(forms.ModelForm):
    class Meta:
        model=Enrollment
        fields=['student','course','enrollment_date']

class StudentGradeForm(forms.ModelForm):
    class Meta:
        model=StudentGrade
        fields=['student','course','grade']

class AttendForm(forms.ModelForm):
    class Meta:
        models=Attend
        fields=['student','course','date','attended']

class StudentFeedbackForm(forms.ModelForm):
    class Meta:
        models=StudentFeedback
        fields=['Student','message','teacher','adminresponse']