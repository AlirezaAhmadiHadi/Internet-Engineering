from django.shortcuts import render, redirect

from projects.forms import CourceForm, StudentForm, RegistrationForm

from .models import course, registration, student


def practices(request):
    return render(request, 'projects/Practices.html')


def practice_three(request):
    Q1students = student.objects.filter(name__startswith='ali')
    Q2students = student.objects.filter(age=22)
    contents = course.objects.get(name='A1').content.all()
    courceID = course.objects.get(name='A1').id
    Registration = registration.objects.filter(courseid=courceID)
    Q3students = []
    for i in Registration:
        Q3students.append(i.studentid)
    context = {'Q1students': Q1students,
               'Q2students': Q2students,
               'contents': contents,
               'Q3students': Q3students,
               }
    return render(request, 'projects/Practice_3/Practice_3.html', context)


def practice_four(request):
    context = {}
    return render(request, 'projects/Practice_4/Practice_4.html', context)


def allStudents(request):
    Students = student.objects.all()
    context = {'Students': Students}
    return render(request, 'projects/Practice_4/Students/Students.html', context)


def createStudent(request):
    form = StudentForm()

    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('allStudents')

    context = {
        'form': form,
        'title': 'Create',
    }
    return render(request, 'projects/Practice_4/Students/Student_form.html', context)


def updateStudent(request, pk):
    Student = student.objects.get(id=pk)

    form = StudentForm(instance=Student)

    if request.method == 'POST':
        form = StudentForm(request.POST, instance=Student)
        if form.is_valid():
            form.save()
            return redirect('allStudents')

    context = {
        'form': form,
        'title': 'Update',
    }
    return render(request, 'projects/Practice_4/Students/Student_form.html', context)


def deleteStudent(request, pk):
    Student = student.objects.get(id=pk)

    form = StudentForm(instance=Student)

    if request.method == 'POST':
        Student.delete()
        return redirect('allStudents')

    context = {
        'form': form,
        'student': Student,
        'title': 'Delete',
    }
    return render(request, 'projects/Practice_4/Students/Delete_Student.html', context)


def allCources(request):
    Cources = course.objects.all()
    context = {'Cources': Cources}
    return render(request, 'projects/Practice_4/Cources/Cources.html', context)


def createCource(request):
    form = CourceForm()

    if request.method == 'POST':
        form = CourceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('allCources')

    context = {
        'form': form,
        'title': 'Create'
    }
    return render(request, 'projects/Practice_4/Cources/Delete_Cource.html', context)


def updateCource(request, pk):
    Cource = course.objects.get(id=pk)

    form = CourceForm(instance=Cource)

    if request.method == 'POST':
        form = CourceForm(request.POST, instance=Cource)
        if form.is_valid():
            form.save()
            return redirect('allCources')

    context = {
        'form': form,
        'title': 'Update',
    }
    return render(request, 'projects/Practice_4/Cources/Cource_form.html', context)


def deleteCource(request, pk):
    Cource = course.objects.get(id=pk)

    form = CourceForm(instance=Cource)

    if request.method == 'POST':
        Cource.delete()
        return redirect('allCources')

    context = {
        'form': form,
        'cource': Cource,
        'title': 'Delete',
    }
    return render(request, 'projects/Practice_4/Cources/Delete_Cource.html', context)


def submitRegistration(request):
    form = RegistrationForm()

    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('practice_4')

    context = {
        'form': form,
    }
    return render(request, 'projects/Practice_4/Registrations/Registration_form.html', context)
