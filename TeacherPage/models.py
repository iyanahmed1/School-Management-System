from django.db import models
from AdminPage.models import Student,Course

class Attendance(models.Model):
    student_id=models.ForeignKey(Student, on_delete=models.CASCADE)
    subject=models.CharField(max_length=50)
    attended=models.BooleanField(default=False)
    date=models.DateField()

    def __str__(self):
        return f"{self.student_id}-{self.subject} on {self.date}"
    
class Grade(models.Model):
    student_id=models.ForeignKey(Student,on_delete=models.CASCADE)
    subject=models.CharField(max_length=50)
    grade=models.CharField(max_length=5)

    def __str__(self):
        return f"{self.student_id} got {self.grade}"
    
class CourseMaterial(models.Model):
    course=models.ForeignKey(Course, on_delete=models.CASCADE)
    material=models.FileField(upload_to='coursematerial/')
    description=models.TextField()

    def __str__(self):
        return self.course
    
class Feedback(models.Model):
    user=models.CharField(max_length=50)
    feedbacktext=models.TextField()
    response=models.TextField(blank=True)
    date=models.DateField()

