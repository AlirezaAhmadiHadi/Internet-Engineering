from django.shortcuts import render
from .models import Project, student, course, registration


def projects(request):
    projects = Project.objects.all()
    context = {"projects": projects}
    return render(request, 'projects/projects.html', context)


def project(request, pk):
    projectObj = Project.objects.get(id=pk)
    return render(request, 'projects/single-project.html', {"project": projectObj})


def intro(request):
    Q1students = student.objects.filter(name__startswith='ali')
    Q2students = student.objects.filter(age=22)
    contents = course.objects.get(name='A1').content.all()
    # Q3students = []
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
    return render(request, 'projects/intro.html', context)
