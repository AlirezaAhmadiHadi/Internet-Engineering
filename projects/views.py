from django.shortcuts import render, redirect

from projects.forms import CourseForm, StudentForm, ContentForm, RegistrationForm

from .models import content, course, registration, student


def home(request):
    return render(request, 'projects/home.html')

# /////////////////////////////
# ///       Students        ///
# /////////////////////////////

def allStudents(request):
    Students = student.objects.all()
    context = {'Students': Students}
    return render(request, 'projects/Students/Students.html', context)

def studentProfile(request, pk):
    Student = student.objects.get(id=pk)
    Courses = []
    for register in registration.objects.filter(studentID=pk):
        Courses.append(register.courseID)
    context = {"Student": Student,
               'Courses': Courses}
    return render(request, "projects/Students/Student-profile.html", context)

def createStudent(request):
    form = StudentForm()

    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('allStudents')

    context = {
        'form': form,
        'title': 'Add',
    }
    return render(request, 'projects/Students/Student_form.html', context)


def updateStudent(request, pk):
    Student = student.objects.get(id=pk)

    form = StudentForm(instance=Student)

    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES, instance=Student)
        if form.is_valid():
            form.save()
            return redirect('allStudents')

    context = {
        'form': form,
        'title': 'Update',
    }
    return render(request, 'projects/Students/Student_form.html', context)


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
    return render(request, 'projects/Students/Delete_Student.html', context)

# /////////////////////////////
# ///       Courses         ///
# /////////////////////////////

def allCourses(request):
    Courses = course.objects.all()
    context = {'Courses': Courses}
    return render(request, 'projects/Courses/Courses.html', context)

def courseProfile(request, pk):
    Course = course.objects.get(id=pk)
    Students = []
    for register in registration.objects.filter(courseID=pk):
        Students.append(register.studentID)
    Contents = Course.content.all()
    context = {"Course": Course,
               'Students': Students,
               'Contents': Contents}
    return render(request, "projects/Courses/Course-profile.html", context)

def createCourse(request):
    form = CourseForm()

    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('allCourses')

    context = {
        'form': form,
        'title': 'Add'
    }
    return render(request, 'projects/Courses/Course_form.html', context)


def updateCourse(request, pk):
    Course = course.objects.get(id=pk)

    form = CourseForm(instance=Course)

    if request.method == 'POST':
        form = CourseForm(request.POST, instance=Course)
        if form.is_valid():
            form.save()
            return redirect('allCourses')

    context = {
        'form': form,
        'title': 'Update',
    }
    return render(request, 'projects/Courses/Course_form.html', context)


def deleteCourse(request, pk):
    Course = course.objects.get(id=pk)

    form = CourseForm(instance=Course)

    if request.method == 'POST':
        Course.delete()
        return redirect('allCourses')

    context = {
        'form': form,
        'course': Course,
        'title': 'Delete',
    }
    return render(request, 'projects/Courses/Delete_Course.html', context)

# /////////////////////////////
# ///       Contents        ///
# /////////////////////////////

def allContents(request):
    Courses = course.objects.all()
    context = {'Courses': Courses}
    return render(request, 'projects/Contents/Contents.html', context)


def createContent(request):
    form = ContentForm()

    if request.method == 'POST':
        form = ContentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('allContents')

    context = {
        'form': form,
        'title': 'Add'
    }
    return render(request, 'projects/Contents/Content_form.html', context)


def updateContent(request, pk):
    Content = content.objects.get(id=pk)

    form = ContentForm(instance=Content)

    if request.method == 'POST':
        form = ContentForm(request.POST, instance=Content)
        if form.is_valid():
            form.save()
            return redirect('allContents')

    context = {
        'form': form,
        'title': 'Update',
    }
    return render(request, 'projects/Contents/Content_form.html', context)


def deleteContent(request, pk):
    Content = content.objects.get(id=pk)

    form = ContentForm(instance=Content)

    if request.method == 'POST':
        Content.delete()
        return redirect('allContents')

    context = {
        'form': form,
        'content': Content,
        'title': 'Delete',
    }
    return render(request, 'projects/Contents/Delete_Content.html', context)

# /////////////////////////////
# ///     Registration      ///
# /////////////////////////////

def submitRegistration(request):
    form = RegistrationForm()

    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('allStudents')

    context = {
        'form': form,
    }
    return render(request, 'projects/Registrations/Registration_form.html', context)
