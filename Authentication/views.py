from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

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
                return redirect("StudentPage:StudentDashboard")
            else:
                messages.error(request, "Unauthorized user!")
        else:
            messages.error(request, "Invalid username or password.")
    
    return render(request, "login.html")

@login_required
def teacher_dashboard(request):
    if not request.user.groups.filter(name="Teachers").exists():
        messages.error(request, "Access Denied!")
        return redirect("Authentication:login")
    return render(request, "Teacherdashboard.html")

@login_required
def student_dashboard(request):
    if not request.user.groups.filter(name="Students").exists():
        messages.error(request, "Access Denied!")
        return redirect("Authentication:login")
    return render(request, "student_dashboard.html")

def logout_user(request):
    logout(request)
    return redirect("home")

