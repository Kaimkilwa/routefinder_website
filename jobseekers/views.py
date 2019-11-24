
from django.shortcuts import render,redirect
from django.core.files.storage import FileSystemStorage
from .forms import JobForm,JobinfoForm
from .models import *

def PersonalInfoView(request):
    form =JobForm
    if request.method == 'POST':
        form = JobForm(request.POST)
        if form.is_valid():
           
            form.save()
            return redirect('jobseekers:jobseekerjobinfor') 
    else:
        form = JobForm()
    return render(request, 'jobseekers/jobseeker.html', {'form': form})

def jobinforView(request):
    form =JobinfoForm
    if request.method == 'POST':
        form = JobinfoForm(request.POST , request.FILES)
        if form.is_valid():
        	form.save()
        	return redirect('jobseekers:joblists') 
    else:
        form = JobinfoForm()
    return render(request, 'jobseekers/jobinfor.html', {'form': form})
def Joblist(request):
    return render(request, 'joblist/joblist.html',{})






 