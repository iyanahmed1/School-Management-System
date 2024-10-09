from django.shortcuts import render
from .forms import StudentForm,TeacherForm, SubjectForm,CourseForm

def studentview(request):
    if request.method=='POST':
        form=StudentForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            form=StudentForm()
        return render(request,'AdminPage/studentview.html',{'form':form})
    
def teacherview(request):
    if request.method=='POST':
        form=TeacherForm(request.POST)
        if form.is_valid():
            form.save()

        else:
            form=TeacherForm()
        return render(request,'AdminPage/teacherview.html',{'form':form})

def subjectview(request):
    if request.method=='POST':
        form=SubjectForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            form=SubjectForm()
        return render(request,'AdminPage/subjectview.html',{'form':form})

def courseview(request):
    if request.method=='POST':
        form=CourseForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            form=CourseForm()
        return render(request,'AdminPage/courseview.html',{'form':form})
    


