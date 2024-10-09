from django.db import models
from StudentPage.models import StudentProfile
from AdminPage.models import Subject,Course,User

class Grade(models.Model):
    student=models.ForeignKey(StudentProfile,on_delete=models.CASCADE)
    subject=models.ForeignKey(Subject,on_delete=models.CASCADE)
    grade=models.CharField(max_length=5)

    def __str__(self):
        return f"{self.student.name} got {self.grade}"
    
class CourseMaterial(models.Model):
    course=models.ForeignKey(Course,on_delete=models.CASCADE)
    material=models.FileField(upload_to='courses_material/')
    description=models.TextField()

    def __str__(self):
        return f"{self.course.name} -{self.description}"

class Attendance(models.Model):
    student=models.ForeignKey(User,on_delete=models.CASCADE)
    subject=models.ForeignKey(Subject,on_delete=models.CASCADE)
    date=models.DateField()
    attended=models.BooleanField(default=False)

    def __str__(self):
        return f"{self.student.username}-{self.subject.name} on {self.date}"


