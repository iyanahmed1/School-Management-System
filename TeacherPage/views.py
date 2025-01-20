from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import AttendanceForm, CourseMaterialForm, GradeForm, FeedbackForm

def manage_attendance(request):
    if request.method == 'POST':
        form = AttendanceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('TeacherPage:')
    else:
        form = AttendanceForm()
    return render(request, 'manage_attendance.html', {'form': form})

def upload_course_material(request):
    if request.method == 'POST':
        form = CourseMaterialForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('TeacherPage')
    else:
        form = CourseMaterialForm()
    return render(request, 'upload_course_material.html', {'form': form})

def manage_grades(request):
    if request.method == 'POST':
        form = GradeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('TeacherPage')
    else:
        form = GradeForm()
    return render(request, 'manage_grades.html', {'form': form})

def submit_feedback(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('TeacherPage')
    else:
        form = FeedbackForm()
    return render(request, 'submit_feedback.html', {'form': form})

def login_teacher(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None and user.groups.filter(name='Teachers').exists():
            login(request, user)
            return redirect('TeacherPage:TeacherDashboard')  
        else:
            messages.error(request, 'Invalid credentials or you are not a teacher.')
    return render(request, 'login_teacher.html')

def teacher_dashboard(request):
    if not request.user.is_authenticated or not request.user.groups.filter(name='Teachers').exists():
        return redirect('LoginTeacher')
    return render(request, 'teacher_dashboard.html')
    

def logout_view(request):
    logout(request)
    return redirect('home')