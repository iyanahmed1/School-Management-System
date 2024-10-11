from django.shortcuts import render,redirect
from .forms import CourseForm, SubjectForm, TeacherForm, StudentForm 

def home(request):
    return render(request,'home.html')

def course_list(request):
    if request.method=='POST':
        form=CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('AdminPage:course_list')
        else:
            form=CourseForm()
        return render(request,'AdminPage/course_list.html'),{'form':form}
        
def course_list(request):
    if request.method=='POST':
        form=CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('AdminPage:course_list')
        else:
            form=CourseForm()
        return render(request,'AdminPage/course_list.html',{'form':form})

def coursecreate(request):
    if request.method=='POST':
        form=CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('AdminPage:coursecreate')
        else:
            form=CourseForm()
        return render(request,'AdminPage/coursecreate.html',{'form':form})
        
def courseupdate(request):
    if request.method=='POST':
        form=CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('AdminPage:courseupdate')
        else:
            form=CourseForm()
        return render(request,'AdminPage/courseupdate.html',{'form':form})
    
def subjectlist(request):
    if request.method=='POST':
        form=SubjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('AdminPage:subjectlist')
        else:
            form=SubjectForm()
        return render (request,'AdminPage/subjectlist.html',{'form':form})
    
def subjectcreate(request):
    if request.method=='POST':
        form=SubjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('AdminPage:subjectcreate')
        else:
            form=SubjectForm()
        return render (request,'AdminPage/subjectcreate.html',{'form':form})

def teacherdetails(request):
    if request.method=='POST':
        form=TeacherForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('AdminPage:teacherdetails')
        else:
            form=SubjectForm()
        return render (request,'AdminPage/teacherdetails.html',{'form':form})
    
def studentlist(request):
    if request.method=='POST':
        form=StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('AdminPage:studentlist')
        else:
            form=SubjectForm()
        return render (request,'AdminPage/studentlist.html',{'form':form})
    
