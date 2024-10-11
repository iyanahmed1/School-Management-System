from django.db import models


class Course(models.Model):
    course_id=models.AutoField(primary_key=True)
    coursename=models.CharField(max_length=60)

    def __str__(self):
        return self.coursename
    
class Subject(models.Model):
    subjectname=models.CharField(max_length=50)
    coursename=models.ForeignKey(Course,on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.subjectname

class Teacher(models.Model):
    teacher_id=models.AutoField(primary_key=True)
    first_name=models.CharField(max_length=60)
    last_name=models.CharField(max_length=60)
    subject=models.ForeignKey(Subject,on_delete=models.CASCADE)
    hiredate=models.DateField()


    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Student(models.Model):
    student_id=models.AutoField(primary_key=True)
    first_name=models.CharField(max_length=60)
    last_name=models.CharField(max_length=60)
    location=models.CharField(max_length=50)
    course=models.ForeignKey(Course,on_delete=models.CASCADE)
    enrolldate=models.DateField()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    


