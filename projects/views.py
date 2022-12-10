from django.shortcuts import render

from .models import course, registration, student

# Create your views here.

def three(request):
    Q1students = student.objects.filter(name__startswith='ali')
    Q2students = student.objects.filter(age=22)
    contents = course.objects.get(name='A1').content.all()
    courceID = course.objects.get(name="A1").id
    Registration = registration.objects.filter(courseid=courceID)
    Q3students = []
    for i in Registration:
        Q3students.append(i.studentid)
    context = {'Q1students': Q1students,
               'Q2students': Q2students,
               'contents': contents,
               'Q3students': Q3students,
               }
    return render(request, 'projects/Practice_3.html', context)