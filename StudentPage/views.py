from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import StudentProfile
from .forms import StudentProfileForm, EnrollmentForm, StudentGradeForm, AttendForm, StudentFeedbackForm

def student_profile(request, id):
    student = get_object_or_404(StudentProfile, id=id)
    return render(request, 'student_profile.html', {'student': student})

def student_enrollment(request):
    if request.method == 'POST':
        form = EnrollmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('FrontOffice:enrollment_success')
    else:
        form = EnrollmentForm()
    return render(request, 'student_enrollment.html', {'form': form})

def student_grade(request):
    if request.method == 'POST':
        form = StudentGradeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('FrontOffice:grade_success')
    else:
        form = StudentGradeForm()
    return render(request, 'student_grade.html', {'form': form})

def student_attendance(request):
    if request.method == 'POST':
        form = AttendForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('FrontOffice:attendance_success')
    else:
        form = AttendForm()
    return render(request, 'student_attendance.html', {'form': form})

def student_feedback(request):
    if request.method == 'POST':
        form = StudentFeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('FrontOffice:feedback_success')
    else:
        form = StudentFeedbackForm()
    return render(request, 'student_feedback.html', {'form': form})

def login_student(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None and user.groups.filter(name='Students').exists():
            login(request, user)
            return redirect('StudentPage:StudentDashboard') 
        else:
            messages.error(request, 'Invalid credentials or you are not a student.')
    return render(request, 'login_student.html')

def student_dashboard(request):
    if not request.user.is_authenticated or not request.user.groups.filter(name='Students').exists():
        return redirect('LoginStudent')  
    return render(request, 'student_dashboard.html')

def logout_view(request):
    logout(request)
    return redirect('home')

def profile_success(request):
    return render(request, 'profile_success.html')  

def enrollment_success(request):
    return render(request, 'enrollment_success.html') 

def grade_success(request):
    return render(request, 'grade_success.html')

def attendance_success(request):
    return render(request, 'attendance_success.html')

def feedback_success(request):
    return render(request, 'feedback_success.html')