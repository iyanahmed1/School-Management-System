from django.db import models
from django.contrib.auth.models import User

class Student(models.Model):
    name=models.CharField(max_length=50)
    location=models.CharField(max_length=50)
    email=models.EmailField()
    parent_no=models.IntegerField()
    enrolled_date=models.DateField()

    def __str__(self):
        return f"{self.user.name} {self.user.enrolled_date}"
    
class Teacher(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    subject=models.CharField(max_length=50)
    hiredate=models.DateField()

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"


class Subject(models.Model):
    name=models.CharField(max_length=100)
    slug=models.SlugField(max_length=50,unique=True)
    description=models.TextField()

    def __str__(self):
        return self.name


class Course(models.Model):
    name=models.CharField(max_length=50)
    teacher=models.ForeignKey(User,on_delete=models.CASCADE)
    subject=models.ForeignKey(Subject,on_delete=models.CASCADE)
    slug=models.SlugField(max_length=50,unique=True)
    created=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    
class Feedback(models.Model):
    sender=models.ForeignKey(User, on_delete=models.CASCADE,related_name='sent_feedback')
    receiver=models.ForeignKey(User,related_name='received_feedback',on_delete=models.CASCADE)
    message=models.TextField()
    date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Feedback from {self.sender.username} to {self.receiver.username} on{self.date}"




