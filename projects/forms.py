from django.forms import ModelForm
from .models import student, course, registration


class StudentForm(ModelForm):
    class Meta:
        model = student
        fields = '__all__'

class CourceForm(ModelForm):
    class Meta:
        model = course
        fields = '__all__'

class RegistrationForm(ModelForm):
    class Meta:
        model = registration
        fields = '__all__'