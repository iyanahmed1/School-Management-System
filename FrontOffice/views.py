from django.shortcuts import render
from .forms import RegistrationForm,AppointmentForm,inquiryForm

def registrationview(request):
    if request.method=='POST':
        form=RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            form=RegistrationForm()
        return render(request,'FrontOffice/registrationview.html',{'form':form})
    
def appointmentview(request):
    if request.method=='POST':
        form=AppointmentForm(request.POST)
        if form.is_valid():
            form.save()

        else:
            form=AppointmentForm()
        return render(request,'FrontOffice/appointmentview.html',{'form':form})

def inquiryview(request):
    if request.method=='POST':
        form=inquiryForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            form=inquiryForm()
        return render(request,'FrontOffice/inquiryview.html',{'form':form})




