from django import forms
from .models import Student,Teacher,Subject,Course

class StudentForm(forms.ModelForm):
    class Meta:
        model=Student
        fields=['student_id','first_name','last_name','location','course']

class TeacherForm(forms.ModelForm):
    class Meta:
        model=Teacher
        fields=['teacher_id','first_name','last_name','subject']

class SubjectForm(forms.ModelForm):
    class Meta:
        model=Subject
        fields=['subjectname']

class CourseForm(forms.ModelForm):
    class Meta:
        model=Course
        fields=['course_id','coursename']