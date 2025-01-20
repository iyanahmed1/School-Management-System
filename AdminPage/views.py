from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import CourseForm, SubjectForm, TeacherForm, StudentForm 
from StudentPage.models import StudentProfile
from .models import Student, Teacher

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
    return render(request,'course_list.html',{'form':form})

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
        form=TeacherForm()
    teachers = Teacher.objects.all()
    return render (request,'teacherdetails.html',{'form':form})

def studentlist(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('AdminPage:studentlist')  
    else:
        form = StudentForm()  
    students = Student.objects.all()  
    return render(request, 'studentlist.html', {'form': form, 'students': students})

def login_admin(request):
    if request.user.is_authenticated:
        print(f"User {request.user.username} is already logged in")
        return redirect('AdminPage:AdminDashboard')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user is not None and user.is_superuser:
            login(request, user)
            print(f"User {user.username} logged in successfully")
            return redirect('AdminPage:AdminDashboard')
        else:
            messages.error(request, 'Invalid credentials or you are not an admin.')

    return render(request, 'login_admin.html')

def admin_dashboard(request):
    if not request.user.is_authenticated or not request.user.groups.filter(name='Admins').exists():
        return redirect('AdminPage:LoginAdmin')  
    return render(request, 'AdminDashboard.html')

def logout_view(request):
    logout(request)
    return redirect('home')

def home(request):
    students = StudentProfile.objects.all()
    return render(request, 'home.html',{'students':students}) 
