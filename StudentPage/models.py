from django.db import models
from django.contrib.auth.models import User
from AdminPage.models import Student,Course,Teacher
from TeacherPage.models import Grade

class StudentProfile(models.Model):
    student=models.CharField(max_length=10)
    student_id = models.ForeignKey(User, on_delete=models.CASCADE)
    course=models.ForeignKey(Course,on_delete=models.CASCADE)
    location=models.CharField(max_length=60)
    email=models.EmailField()
    phone=models.CharField(max_length=10)
    date_of_birth=models.DateField()

    def __str__(self):
        return f"{self.student_id} {self.student.last_name}"
    
class Enrollment(models.Model):
    student=models.ForeignKey(Student, on_delete=models.CASCADE)
    course=models.ForeignKey(Course,on_delete=models.CASCADE)
    enrollment_date=models.DateField()

    def __str__(self):
        return f"{self.student.first_name} enrolled in {self.course.coursename}"
    
class Attend(models.Model):
    student=models.ForeignKey(Student,on_delete=models.CASCADE)
    course=models.ForeignKey(Course,on_delete=models.CASCADE)
    date=models.DateField()
    attended=models.BooleanField(default=False)

    def __str__(self):
        return f"{self.student.first_name} attended {self.course.coursename}"
    
class StudentGrade(models.Model):
    student=models.ForeignKey(Student,on_delete=models.CASCADE)
    course=models.ForeignKey(Course,on_delete=models.CASCADE)
    grade=models.ForeignKey(Grade,on_delete=models.CASCADE)
    date=models.DateField()

    def __str__(self):
        return f"{self.student.first_name} -{self.course.coursename} got {self.grade}"

class StudentFeedback(models.Model):
    student=models.ForeignKey(Student,on_delete=models.CASCADE)
    message=models.TextField()
    teacher=models.ForeignKey(Teacher,on_delete=models.CASCADE)
    adminresponse=models.TextField(blank=True)
    submitdate=models.DateField()

