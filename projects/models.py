from django.db import models
import uuid
from users.models import Profile

# Create your models here.

class course(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, editable=False)
    name = models.CharField(max_length=50, blank=True)
    content = models.ManyToManyField('content', blank=True)
    course_image = models.ImageField(null=True, blank=True, default="default-course.jpg")
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class student(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, editable=False)
    name = models.CharField(max_length=50, blank=True)
    age = models.IntegerField(default=0, blank=True)
    studentNumber = models.IntegerField(default=0, blank=True)
    student_image = models.ImageField(null=True, blank=True, default="default.jpg")
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name    

class content(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, editable=False)
    des = models.CharField(max_length=2000, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.des

class registration(models.Model):
    owner = models.ForeignKey(Profile, null=True, blank=True, on_delete=models.SET_NULL)
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, editable=False)
    courseID = models.ForeignKey('course', on_delete=models.CASCADE)
    studentID = models.ForeignKey('student', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.studentID.name} to {self.courseID.name}"