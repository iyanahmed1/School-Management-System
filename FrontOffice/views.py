from django.shortcuts import render, redirect
from .forms import StudentRegistrarionForm,InquiryForm, AppointmentForm, NotificationForm

def register_student(request):
    pass

def submit_inquiry(request):
    if request.method == "POST":
        form = InquiryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inquiry_success')
    else:
        form = InquiryForm()
    return render(request, 'submit_inquiry.html', {'form': form})

def schedule_appointment(request):
    if request.method == "POST":
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('appointment_success')
    else:
        form = AppointmentForm()
    return render(request, 'schedule_appointment.html', {'form': form})

def send_notification(request):
    if request.method == "POST":
        form = NotificationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('notification_success')
    else:
        form = NotificationForm()
    return render(request, 'send_notification.html', {'form': form})

