from django.shortcuts import render, redirect
from .forms import StudentRegistrarionForm,InquiryForm, AppointmentForm, NotificationForm

def register_student(request):
    if request.method == "POST":
        form = StudentRegistrarionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('FrontOffice:register_success')  
    else:
        form = StudentRegistrarionForm()
    return render(request, 'register_student.html', {'form': form})

def submit_inquiry(request):
    if request.method == "POST":
        form = InquiryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('FrontOffice:inquiry_success')
    else:
        form = InquiryForm()
    return render(request, 'submit_inquiry.html', {'form': form})

def schedule_appointment(request):
    if request.method == "POST":
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('FrontOffice:appointment_success')
    else:
        form = AppointmentForm()
    return render(request, 'schedule_appointment.html', {'form': form})

def send_notification(request):
    if request.method == "POST":
        form = NotificationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('FrontOffice:notification_success')
    else:
        form = NotificationForm()
    return render(request, 'send_notification.html', {'form': form})

def inquiry_success(request):
    return render(request, 'inquiry_success.html')

def appointment_success(request):
    return render(request, 'appointment_success.html')

def notification_success(request):
    return render(request, 'notification_success.html')

def register_success(request):
    return render(request, 'register_success.html')