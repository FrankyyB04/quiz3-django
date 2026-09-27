from django.shortcuts import render
from .models import Student

# Create your views here.

def StudentPage(request):
    students = Student.objects.all().values()
    return render(request, 'homepage.html', {'students' : students})

def StudentDetails(request, id):
    students = Student.objects.get(id=id)
    return render(request, 'details.html', {'students' : students})

