from django.shortcuts import render
from django.http import HttpResponse
from .models import Student
# Create your views here.

'''Views are of two types
Function based Views
Class based Views'''

def home(request):
    # return HttpResponse('This is school home view')
    return render(request, 'base.html', {"username":"saikiran"})

def about(request):
    return HttpResponse('This is about view')

def admissions(request):
    # return HttpResponse('This is admission view')
    if request.method == 'POST':
        name = request.POST['name']
        address = request.POST['address']
        father_name = request.POST['father_name']
        age = request.POST['age']
        image = request.FILES.get('image')

        k = Student(name=name, address=address, father_name=father_name, age=age, image=image)
        k.save()

    return render(request, 'admission.html')

def admissionsReport(request):
    # return HttpResponse('This is admission report view')
    StudentInfo = Student.objects.all()
    return render(request, 'admission_report.html', {"StudentInfo":StudentInfo})
