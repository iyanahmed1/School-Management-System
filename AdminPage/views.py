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
        return render(request,'course_list.html'),{'form':form}

def register_student(request):
    if request.method=='POST':
        form=CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('AdminPage:register_student')
        else:
            form=CourseForm()
        return render(request,'register_student.html.html',{'form':form})


def coursecreate(request):
    if request.method=='POST':
        form=CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('AdminPage:coursecreate')
        else:
            form=CourseForm()
        return render(request,'coursecreate.html',{'form':form})
        
def courseupdate(request):
    if request.method=='POST':
        form=CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('AdminPage:courseupdate')
        else:
            form=CourseForm()
        return render(request,'courseupdate.html',{'form':form})
    
def subjectlist(request):
    if request.method=='POST':
        form=SubjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('AdminPage:subjectlist')
        else:
            form=SubjectForm()
        return render (request,'subjectlist.html',{'form':form})
    
def subjectcreate(request):
    if request.method=='POST':
        form=SubjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('AdminPage:subjectcreate')
        else:
            form=SubjectForm()
        return render (request,'subjectcreate.html',{'form':form})

def teacherdetails(request):
    if request.method=='POST':
        form=TeacherForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('AdminPage:teacherdetails')
        else:
            form=SubjectForm()
        return render (request,'teacherdetails.html',{'form':form})
    
def studentlist(request):
    if request.method=='POST':
        form=StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('AdminPage:studentlist')
        else:
            form=SubjectForm()
        return render (request,'studentlist.html',{'form':form})
    
def home(request):
    return render(request, 'home.html') 
