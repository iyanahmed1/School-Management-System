from django.db import models
from django.contrib.auth.models import User

class Registration(models.Model):
    student_name=models.CharField(max_length=50)
    location=models.CharField(max_length=50)
    email=models.EmailField()
    parent_no=models.IntegerField()
    course=models.CharField(max_length=50)

    def __str__(self):
        return f"{self.student_name} - {self.course}"
    
class inquiry(models.Model):
    people=[
        ('Student','student'),
        ('Parent','parent'),
        ('Vistor','vistor'),
    ]
    email=models.EmailField()
    note=models.TextField()
    date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.people} inquired about {self.note} on {self.date}"
    
class Appointment(models.Model):
    teacher=models.ForeignKey(User,on_delete=models.CASCADE,related_name='appointment schedule for teacher')
    student=models.ForeignKey(User,on_delete=models.CASCADE,related_name='appointment for student')
    date=models.DateTimeField()
    reason=models.TextField()

    def __str__(self):
        return f"Appointment made for {self.teacher.username} on {self.date} by {self.student.username}"
    
class Notification(models.Model):
    student=models.ForeignKey(User,on_delete=models.CASCADE)
    parent=models.ForeignKey(User,on_delete=models.CASCADE)
    message=models.TextField()
    datesent=models.DateTimeField(auto_now_add=True)

    def __str__(self):
            return f"Notification sent to{self.student.username}"
        