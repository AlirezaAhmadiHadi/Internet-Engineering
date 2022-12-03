from django.contrib import admin
from .models import Project, Review, Tag
from .models import student, registration, content, course

# Register your models here.
admin.site.register(Project)
admin.site.register(Review)
admin.site.register(Tag)

admin.site.register(student)
admin.site.register(registration)
admin.site.register(content)
admin.site.register(course)
