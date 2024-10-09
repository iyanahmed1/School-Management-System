from django import forms 
from .models import Subject,Course,Student,Teacher


class SubjectForm(forms.ModelForm):
    class Meta:
        model=Subject
        field=['name','slug']

class CourseForm(forms.ModelForm):
    class Meta:
        model=Course
        fields=['name','teacher','subject']

class TeacherForm(forms.ModelForm):
    class Meta:
        model=Teacher
        fields=['first_name','last_name','subject']

class StudentForm(forms.ModelForm):
    class Meta:
        model=Student
        fields=['name','enrolled_date']