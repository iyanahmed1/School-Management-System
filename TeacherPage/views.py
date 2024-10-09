from django.shortcuts import render
from .forms import GradeForm, AttendanceForm

def gradeview(request):
    if request.method=='POST':
        form=GradeForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            form=GradeForm()
        return render(request,'StudentPage/gradeview.html',{'form':form})
    
def attendanceview(request):
    if request.method=='POST':
        form=AttendanceForm(request.POST)
        if form.is_valid():
            form.save()

        else:
            form=AttendanceForm()
        return render(request,'StudentPage/attendanceview.html',{'form':form})

