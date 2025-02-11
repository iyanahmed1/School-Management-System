from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import StudentRegistrarionForm,InquiryForm, AppointmentForm, NotificationForm

@login_required
def frontoffice_dashboard(request):
    if not request.user.groups.filter(name="FrontOffice").exists():
        messages.error(request, "Access Denied!")
        return redirect("home")
    
    return render(request, "frontoffice_dashboard.html")

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

def login_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.groups.filter(name="Teachers").exists():
                return redirect("TeacherPage:Teacherdashboard")
            elif user.groups.filter(name="Students").exists():
                return redirect("StudentPage:student_dashboard")
            elif user.groups.filter(name="FrontOffice").exists():
                return redirect("FrontOffice:frontoffice_dashboard")  
            else:
                messages.error(request, "Unauthorized user!")
        else:
            messages.error(request, "Invalid username or password.")

    return render(request, "login.html")

def staff_dashboard(request):
    if not request.user.is_authenticated or not request.user.groups.filter(name='Staff').exists():
        return redirect('FrontOffice:Loginuser')  
    return render(request, 'frontoffice_dashboard.html')

def logout_view(request):
    logout(request)
    return redirect('home')

def inquiry_success(request):
    return render(request, 'inquiry_success.html')

def appointment_success(request):
    return render(request, 'appointment_success.html')

def notification_success(request):
    return render(request, 'notification_success.html')

def register_success(request):
    return render(request, 'register_success.html')