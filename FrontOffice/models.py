from django.db import models
from AdminPage.models import Student

class Inquiry(models.Model):
    name=models.CharField(max_length=60)
    email=models.EmailField()
    message=models.TextField()
    status=models.CharField(max_length=60, default='open')
    created=models.DateTimeField(auto_now_add=True)

class Appointment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    teacher = models.CharField(max_length=255)
    date = models.DateField()
    time = models.TimeField()
    status = models.CharField(max_length=50, default='Scheduled')

class Notification(models.Model):
    recipient=models.EmailField()
    message=models.TextField()
    createdate=models.DateTimeField(auto_now_add=True)

