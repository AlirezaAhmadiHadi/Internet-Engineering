from django.contrib import admin
from .models import content, course, registration, student

# Register your models here.

admin.site.register(student)
admin.site.register(registration)
admin.site.register(content)
admin.site.register(course)