from django.shortcuts import render, redirect
from .forms import AttendanceForm, CourseMaterialForm, GradeForm, FeedbackForm

def manage_attendance(request):
    if request.method == 'POST':
        form = AttendanceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('TeacherPage')
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
