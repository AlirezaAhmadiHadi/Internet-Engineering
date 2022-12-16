from django.db import models
import uuid

# Create your models here.

class course(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, editable=False)
    name = models.CharField(max_length=50, blank=True)
    content = models.ManyToManyField('content', blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class student(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, editable=False)
    name = models.CharField(max_length=50, blank=True)
    age = models.IntegerField(default=0, blank=True)
    sudentNumber = models.IntegerField(default=0, blank=True)
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
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, editable=False)
    courseid = models.ForeignKey('course', on_delete=models.CASCADE)
    studentid = models.ForeignKey('student', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
