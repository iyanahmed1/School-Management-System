from django.shortcuts import render, redirect
from .forms import StudentProfileForm, EnrollmentForm, StudentGradeForm, AttendForm, StudentFeedbackForm

def student_profile(request):
    if request.method == 'POST':
        form = StudentProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('FrontOffice:profile_success')
    else:
        form = StudentProfileForm()
    return render(request, 'FrontOffice/student_profile.html', {'form': form})

def student_enrollment(request):
    if request.method == 'POST':
        form = EnrollmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('FrontOffice:enrollment_success')
    else:
        form = EnrollmentForm()
    return render(request, 'FrontOffice/student_enrollment.html', {'form': form})

def student_grade(request):
    if request.method == 'POST':
        form = StudentGradeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('FrontOffice:grade_success')
    else:
        form = StudentGradeForm()
    return render(request, 'FrontOffice/student_grade.html', {'form': form})

def student_attendance(request):
    if request.method == 'POST':
        form = AttendForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('FrontOffice:attendance_success')
    else:
        form = AttendForm()
    return render(request, 'FrontOffice/student_attendance.html', {'form': form})

def student_feedback(request):
    if request.method == 'POST':
        form = StudentFeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('FrontOffice:feedback_success')
    else:
        form = StudentFeedbackForm()
    return render(request, 'FrontOffice/student_feedback.html', {'form': form})
