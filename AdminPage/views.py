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
        if request.user.is_superuser or request.user.groups.filter(name='Admins').exists():
            return redirect('AdminPage:AdminDashboard')
        else:
            logout(request)  
            messages.error(request, 'You are not authorized to access the admin panel.')
            return redirect('AdminPage:LoginAdmin')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user is not None and (user.is_superuser or user.groups.filter(name='Admins').exists()):
            login(request, user)
            return redirect('AdminPage:AdminDashboard')
        else:
            messages.error(request, 'Invalid credentials or insufficient permissions.')

    return render(request, 'login_admin.html')


def admin_dashboard(request):
    if not request.user.is_authenticated:
        messages.error(request, 'Please log in to access the admin dashboard.')
        return redirect('AdminPage:LoginAdmin')
    
    if not request.user.groups.filter(name='Admins').exists() and not request.user.is_superuser:
        messages.error(request, 'You are not authorized to access this page.')
        return redirect('AdminPage:LoginAdmin')

    return render(request, 'AdminDashboard.html')

def logout_view(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect('AdminPage:LoginAdmin')

def home(request):
    students = StudentProfile.objects.all()
    return render(request, 'home.html',{'students':students}) 
