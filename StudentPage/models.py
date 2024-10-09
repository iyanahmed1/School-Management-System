from django.db import models
from AdminPage.models import Course

class StudentProfile(models.Model):
    name=models.CharField(max_length=50)
    location=models.CharField(max_length=50)
    email=models.EmailField()
    parent_no=models.IntegerField()
    enrolled_date=models.DateField()

    def __str__(self):
        return self.name
    
class Enroll(models.Model):
    name=models.ForeignKey(StudentProfile,on_delete=models.CASCADE)
    course=models.ForeignKey(Course,on_delete=models.CASCADE)
    date_enrolled=models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}-{self.course.name}"

