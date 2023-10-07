from django.shortcuts import render,redirect
from django.http import HttpResponse
from . import forms 
from . import models
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    return render(request,'hr_app/home.html')

def employee(request):
    return render(request,'hr_app/employee.html')

def employee_list(request):
    employee=models.Employee.objects.all()
    return render(request,'hr_app/users.html',{'employee': employee})


def contact_form(request):
    print("$$$$$$")
    form = forms.Employeeform() 
    if request.method=="POST":
        form = forms.Employeeform(request.POST)
        if form.is_valid():
            print('Form is valid')
            form.save()
            return redirect('/empdata')
        else:
             form = forms.Employeeform()
          
    return render(request,'hr_app/contact.html',{'form': form})


def logout(request):
    return render(request,'hr_app/logout.html')

@login_required
def hr(request):
    return render(request,'hr_app/hr_main.html')


def submit_holiday(request):
    if request.method == 'POST':
        form = forms.HolidayForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/list')  
    else:
        form = forms.HolidayForm()
    return render(request, 'hr_app/calender.html', {'form': form})


def holiday_list(request):
    holidays = models.Holiday.objects.all().order_by('date')
    return render(request, 'hr_app/holiday_list.html', {'holidays': holidays})



def submit_news(request):
    if request.method == 'POST':
        form = forms.NewsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/news_list')  
    else:
        form = forms.NewsForm()
    return render(request, 'hr_app/news.html', {'form': form})

def news_list(request):
    news = models.NewsArticle.objects.all()
    return render(request, 'hr_app/news_list.html', {'news': news})

def update_employee(request, pk):
    employee = models.Employee.objects.get(pk=pk)
    if request.method == 'POST':
        form = forms.Employeeform(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('/empdata')
    else:
        form = forms.Employeeform(instance=employee)
    return render(request,'hr_app/contact.html', {'form': form})

def delete_employee(request, pk):
    employee = models.Employee.objects.get(pk=pk)
    employee.delete()
    return redirect('/empdata')













