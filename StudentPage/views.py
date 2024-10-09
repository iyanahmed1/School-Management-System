from django.shortcuts import render
from .forms import StudentProfileForm,EnrollForm

def studentprofileview(request):
    if request.method=='POST':
        form=StudentProfileForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            form=StudentProfileForm()
        return render(request,'StudentPage/studentprofileview.html',{'form':form})
    
def enrollview(request):
    if request.method=='POST':
        form=EnrollForm(request.POST)
        if form.is_valid():
            form.save()

        else:
            form=EnrollForm()
        return render(request,'StudentPage/enrollview.html',{'form':form})
