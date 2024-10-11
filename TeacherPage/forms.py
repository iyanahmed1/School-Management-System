from django import forms
from .models import Attendance,CourseMaterial,Grade,Feedback

class AttendanceForm(forms.ModelForm):
    class Meta:
        model=Attendance
        fields=['student_id','subject','attended','date']

class CourseMaterialForm(forms.ModelForm):
    class Meta:
        model=CourseMaterial
        fields=['course','material']

class GradeForm(forms.ModelForm):
    class Meta:
        model=Grade
        fields=['student_id','subject','grade']

class FeedbackForm(forms.ModelForm):
    class Meta:
        model=Feedback
        fields=['user','feedbacktext','date']